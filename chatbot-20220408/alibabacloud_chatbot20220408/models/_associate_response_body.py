# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class AssociateResponseBody(DaraModel):
    def __init__(
        self,
        associate: List[main_models.AssociateResponseBodyAssociate] = None,
        message_id: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.associate = associate
        self.message_id = message_id
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.associate:
            for v1 in self.associate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Associate'] = []
        if self.associate is not None:
            for k1 in self.associate:
                result['Associate'].append(k1.to_map() if k1 else None)

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associate = []
        if m.get('Associate') is not None:
            for k1 in m.get('Associate'):
                temp_model = main_models.AssociateResponseBodyAssociate()
                self.associate.append(temp_model.from_map(k1))

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self



class AssociateResponseBodyAssociate(DaraModel):
    def __init__(
        self,
        meta: str = None,
        title: str = None,
    ):
        self.meta = meta
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['Meta'] = self.meta

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

