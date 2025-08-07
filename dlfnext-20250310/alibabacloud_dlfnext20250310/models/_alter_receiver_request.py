# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class AlterReceiverRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        receiver_name: str = None,
    ):
        self.comment = comment
        self.receiver_name = receiver_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.receiver_name is not None:
            result['receiverName'] = self.receiver_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('receiverName') is not None:
            self.receiver_name = m.get('receiverName')

        return self

