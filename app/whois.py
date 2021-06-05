import asyncio
import shlex

from asyncwhois.errors import QueryError
from whois_parser import WhoisParser

from . import schemas


def parse(raw_text: str, hostname: str) -> schemas.WhoisRecord:
    parser = WhoisParser()
    record = parser.parse(raw_text, hostname=hostname)

    return schemas.WhoisRecord.parse_obj(record.to_dict())


async def whois(hostname: str, timeout: float = 3.0) -> schemas.WhoisRecord:
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
