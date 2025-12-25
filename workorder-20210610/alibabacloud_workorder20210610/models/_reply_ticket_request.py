# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ReplyTicketRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        encrypt: bool = None,
        file_name_list: List[str] = None,
        ticket_id: str = None,
        uid: str = None,
    ):
        # Content of the ticket reply
        # 
        # This parameter is required.
        self.content = content
        # Encryption status
        # 
        # This parameter is required.
        self.encrypt = encrypt
        # The list of attachment names, GetAttachmentUploadUrl the ObjectKey field returned by the interface.
        self.file_name_list = file_name_list
        # The ID of the ticket.
        # 
        # This parameter is required.
        self.ticket_id = ticket_id
        # Alibaba Cloud UID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt

        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')

        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

