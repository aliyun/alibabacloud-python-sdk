# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetReportTemplateByNameResponseBody(DaraModel):
    def __init__(
        self,
        default_received_convs: List[main_models.GetReportTemplateByNameResponseBodyDefaultReceivedConvs] = None,
        default_receivers: List[main_models.GetReportTemplateByNameResponseBodyDefaultReceivers] = None,
        fields: List[main_models.GetReportTemplateByNameResponseBodyFields] = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        user_name: str = None,
        userid: str = None,
    ):
        self.default_received_convs = default_received_convs
        self.default_receivers = default_receivers
        self.fields = fields
        self.id = id
        self.name = name
        # requestId
        self.request_id = request_id
        self.user_name = user_name
        self.userid = userid

    def validate(self):
        if self.default_received_convs:
            for v1 in self.default_received_convs:
                 if v1:
                    v1.validate()
        if self.default_receivers:
            for v1 in self.default_receivers:
                 if v1:
                    v1.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['defaultReceivedConvs'] = []
        if self.default_received_convs is not None:
            for k1 in self.default_received_convs:
                result['defaultReceivedConvs'].append(k1.to_map() if k1 else None)

        result['defaultReceivers'] = []
        if self.default_receivers is not None:
            for k1 in self.default_receivers:
                result['defaultReceivers'].append(k1.to_map() if k1 else None)

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.userid is not None:
            result['userid'] = self.userid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.default_received_convs = []
        if m.get('defaultReceivedConvs') is not None:
            for k1 in m.get('defaultReceivedConvs'):
                temp_model = main_models.GetReportTemplateByNameResponseBodyDefaultReceivedConvs()
                self.default_received_convs.append(temp_model.from_map(k1))

        self.default_receivers = []
        if m.get('defaultReceivers') is not None:
            for k1 in m.get('defaultReceivers'):
                temp_model = main_models.GetReportTemplateByNameResponseBodyDefaultReceivers()
                self.default_receivers.append(temp_model.from_map(k1))

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.GetReportTemplateByNameResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('userid') is not None:
            self.userid = m.get('userid')

        return self

class GetReportTemplateByNameResponseBodyFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        sort: int = None,
        type: int = None,
    ):
        self.field_name = field_name
        self.sort = sort
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetReportTemplateByNameResponseBodyDefaultReceivers(DaraModel):
    def __init__(
        self,
        user_name: str = None,
        userid: str = None,
    ):
        self.user_name = user_name
        self.userid = userid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.userid is not None:
            result['Userid'] = self.userid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Userid') is not None:
            self.userid = m.get('Userid')

        return self

class GetReportTemplateByNameResponseBodyDefaultReceivedConvs(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        title: str = None,
    ):
        self.conversation_id = conversation_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

