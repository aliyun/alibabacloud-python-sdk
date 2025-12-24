# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectionTicketResponseBody(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        request_id: str = None,
        task_code: str = None,
        task_id: str = None,
        task_message: str = None,
        task_status: str = None,
        ticket: str = None,
    ):
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The ID of the request.
        self.request_id = request_id
        # Before you use the credential, you must Base64 decode the content of the credential, save the credential as an xxx.ica file, and then open the file. Python sample code:
        # 
        #     import base64
        #     response = {
        #         "Ticket": "W0VuY29kaW5nXQ0KSW5wdXRFbmNvZGluZz1V********",
        #         "RequestId": "1CBAFFAB-B697-4049-A9B1-67E1FC5F****",
        #     }
        #     f = open (\\"xxx.ica\\", \\"w\\")
        #     out = base64.b64decode(response[\\"Ticket\\"])
        #     f.write(out)
        #     f.close()
        self.task_code = task_code
        # The ID of the cloud computer connection task.
        self.task_id = task_id
        # The ID of the connection task.
        self.task_message = task_message
        # The task status.
        # 
        # Valid values:
        # 
        # *   FAILED: The credential fails to be obtained.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RUNNING: The credential is being obtained.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   FINISHED: The credential is obtained.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.task_status = task_status
        # The credentials for connecting to the cloud computer.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_code is not None:
            result['TaskCode'] = self.task_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_message is not None:
            result['TaskMessage'] = self.task_message

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

