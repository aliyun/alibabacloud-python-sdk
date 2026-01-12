# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWebTerminalResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        web_terminal_url: str = None,
    ):
        # The request ID which is used for diagnostics and Q\\&A.
        self.request_id = request_id
        # The WebSocket URI for accessing the container. You must build a WebSocket client. For more information about the communication format, see the following code:
        # 
        #     ws = new WebSocket(
        #       `wss://xxxxx`,
        #     );
        #     ws.onopen = function open() {
        #       console.warn(\\"connected\\");
        #       term.write(\\"\\r\\");
        #     };
        # 
        #     ws.onclose = function close() {
        #       console.warn(\\"disconnected\\");
        #       term.write(\\"Connection closed\\");
        #     };
        # 
        #     // Return the following information in the backend.
        #     ws.onmessage = function incoming(event) {
        #       const msg = JSON.parse(event.data);
        #       console.warn(msg);
        #       if (msg.operation === \\"stdout\\") {
        #         term.write(msg.data);
        #       } else {
        #         console.warn(\\"invalid msg operation: \\" + msg);
        #       }
        #     };
        # 
        #     // Enter the following code in the console.
        #     term.onData(data => {
        #       const msg = { operation: \\"stdin\\", data: data };
        #       ws.send(JSON.stringify(msg));
        #     });
        # 
        #     term.onResize(size => {
        #       const msg = { operation: \\"resize\\", cols: size.cols, rows: size.rows };
        #       ws.send(JSON.stringify(msg));
        #     });
        # 
        #     fitAddon.fit();
        #     };
        self.web_terminal_url = web_terminal_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.web_terminal_url is not None:
            result['WebTerminalUrl'] = self.web_terminal_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WebTerminalUrl') is not None:
            self.web_terminal_url = m.get('WebTerminalUrl')

        return self

