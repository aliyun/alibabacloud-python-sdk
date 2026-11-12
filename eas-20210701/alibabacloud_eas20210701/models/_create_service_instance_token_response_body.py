# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceInstanceTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        streamlog_url: str = None,
        token: str = None,
        url: str = None,
        workbench_url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # This parameter is not used.
        self.streamlog_url = streamlog_url
        # The authentication token.
        self.token = token
        # The WebSocket URL.
        self.url = url
        # The URL used to log on to the container through Workbench. After you log on to the service instance, the returned messages use the WebSocket text message format. The message content is Base64-encoded. Refer to the following script for processing.
        # 
        # ```python
        # #!/usr/bin/env python3
        # """macOS/Linux: python webshell_minimal.py \\"wss://...\\"; Ctrl+] disconnects."""
        # import argparse
        # import base64
        # import codecs
        # import getpass
        # import json
        # import os
        # import select
        # import shutil
        # import sys
        # import termios
        # import threading
        # import tty
        # 
        # import websocket
        # 
        # 
        # def main():
        #     parser = argparse.ArgumentParser(description=__doc__)
        #     parser.add_argument(\\"url\\", help=\\"Url from CreateServiceInstanceToken(ActionType=WebShell)\\")
        #     args = parser.parse_args()
        #     if not sys.stdin.isatty():
        #         parser.error(\\"Run from an interactive macOS/Linux terminal\\")
        #     token = os.environ.get(\\"WEBSHELL_TOKEN\\") or getpass.getpass(\\"Token: \\")
        #     ws = websocket.create_connection(args.url, header={\\"Authorization\\": \\"Bearer \\" + token.strip()},
        #                                      subprotocols=[\\"webtty\\"], timeout=10)
        #     ws.settimeout(None)
        #     stopped = threading.Event()
        # 
        #     def receive():
        #         try:
        #             while not stopped.is_set():
        #                 message = ws.recv()  # websocket-client automatically replies to control Ping frames.
        #                 if not message:
        #                     break
        #                 if isinstance(message, str) and message[0] == \\"1\\":
        #                     sys.stdout.buffer.write(base64.b64decode(message[1:], validate=True))
        #                     sys.stdout.buffer.flush()  # Preserve terminal escape sequences and UTF-8 bytes.
        #                 # \\"2\\" is webtty Pong; other types need no handling in this terminal client.
        #         except (websocket.WebSocketException, OSError, ValueError):
        #             pass
        #         finally:
        #             stopped.set()
        # 
        #     fd = sys.stdin.fileno()
        #     previous = termios.tcgetattr(fd)
        #     decoder = codecs.getincrementaldecoder(\\"utf-8\\")()
        #     print(\\"Connected. Ctrl+] disconnects; Ctrl+C is sent to the remote shell.\\", flush=True)
        #     reader = threading.Thread(target=receive, daemon=True)
        #     try:
        #         tty.setraw(fd)
        #         reader.start()
        #         size = None
        #         while not stopped.is_set():
        #             current = shutil.get_terminal_size((80, 24))
        #             if current != size:
        #                 ws.send(\\"3\\" + json.dumps({\\"columns\\": current.columns, \\"rows\\": current.lines}))
        #                 size = current
        #             if select.select([fd], [], [], 0.2)[0]:
        #                 data = os.read(fd, 4096)
        #                 if not data or b\\"\\x1d\\" in data:  # Ctrl+]
        #                     break
        #                 text = decoder.decode(data)  # Do not split a UTF-8 character across Text messages.
        #                 if text:
        #                     ws.send(\\"1\\" + text)  # Raw input, NOT base64 and NOT a JSON wrapper.
        #     finally:
        #         termios.tcsetattr(fd, termios.TCSADRAIN, previous)
        #         stopped.set()
        #         try:
        #             ws.send_close()
        #         except (websocket.WebSocketException, OSError):
        #             pass
        #         ws.shutdown()
        #         if reader.ident is not None:
        #             reader.join(timeout=1)
        #         print(\\"
        # Disconnected.\\", flush=True)
        # 
        # 
        # if __name__ == \\"__main__\\":
        #     try:
        #         main()
        #     except websocket.WebSocketBadStatusException as exc:
        #         sys.exit(f\\"WebSocket handshake failed: HTTP {exc.status_code}\\")
        #     except (websocket.WebSocketException, OSError, UnicodeError, KeyboardInterrupt) as exc:
        #         sys.exit(f\\"WebShell stopped: {type(exc).__name__}\\")
        # 
        # ```
        self.workbench_url = workbench_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.streamlog_url is not None:
            result['StreamlogUrl'] = self.streamlog_url

        if self.token is not None:
            result['Token'] = self.token

        if self.url is not None:
            result['Url'] = self.url

        if self.workbench_url is not None:
            result['WorkbenchUrl'] = self.workbench_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamlogUrl') is not None:
            self.streamlog_url = m.get('StreamlogUrl')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkbenchUrl') is not None:
            self.workbench_url = m.get('WorkbenchUrl')

        return self

