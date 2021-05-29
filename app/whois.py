import asyncio
import shlex
from datetime import datetime
from typing import Dict, Optional, Union

from asyncwhois.errors import NotFoundError, QueryError
from asyncwhois.parser import WhoIsParser

from . import schemas


def build_parser(hostname: str) -> WhoIsParser:
    tld = hostname.split(".")[-1]
    return WhoIsParser(tld)


def parse(raw: str, hostname: str) -> schemas.ParsedWhoisResult:
    output: Dict[str, Optional[Union[str, datetime]]] = {
        "hostname": hostname,
        "raw": raw,
    }
    try:
        parser = build_parser(hostname)
        parser.parse(raw)
        output.update(parser.parser_output)
    except NotFoundError:
        pass

    return schemas.ParsedWhoisResult.parse_obj(output)


async def whois(hostname: str, timeout: float = 3.0) -> schemas.ParsedWhoisResult:
    # open a new process for "whois" command
    cmd = f"whois {shlex.quote(hostname)}"
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    try:
        # block for query_result
        query_result_, _ = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        query_result = query_result_.decode(errors="ignore")
        query_result = query_result.strip()
    except asyncio.TimeoutError:
        raise QueryError(
            f'The shell command "whois {hostname}" exceeded timeout of {timeout} seconds'
        )

    return parse(query_result, hostname)
