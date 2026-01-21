# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PushingTarget(DaraModel):
    def __init__(
        self,
        arn: str = None,
        create_time: str = None,
        description: str = None,
        http_request_target: main_models.PushingTargetHttpRequestTarget = None,
        name: str = None,
        range: str = None,
        template_uuid: str = None,
        type: str = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        self.arn = arn
        self.create_time = create_time
        self.description = description
        self.http_request_target = http_request_target
        # This parameter is required.
        self.name = name
        self.range = range
        self.template_uuid = template_uuid
        self.type = type
        self.update_time = update_time
        self.user_id = user_id
        self.uuid = uuid

    def validate(self):
        if self.http_request_target:
            self.http_request_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.http_request_target is not None:
            result['HttpRequestTarget'] = self.http_request_target.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.range is not None:
            result['Range'] = self.range

        if self.template_uuid is not None:
            result['TemplateUuid'] = self.template_uuid

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HttpRequestTarget') is not None:
            temp_model = main_models.PushingTargetHttpRequestTarget()
            self.http_request_target = temp_model.from_map(m.get('HttpRequestTarget'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('TemplateUuid') is not None:
            self.template_uuid = m.get('TemplateUuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class PushingTargetHttpRequestTarget(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        encrypt_signature_key: str = None,
        encrypt_string: str = None,
        encrypt_timestamp_key: str = None,
        headers: List[main_models.PushingTargetHttpRequestTargetHeaders] = None,
        method: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.encrypt_signature_key = encrypt_signature_key
        self.encrypt_string = encrypt_string
        self.encrypt_timestamp_key = encrypt_timestamp_key
        self.headers = headers
        self.method = method
        self.url = url

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.encrypt_signature_key is not None:
            result['EncryptSignatureKey'] = self.encrypt_signature_key

        if self.encrypt_string is not None:
            result['EncryptString'] = self.encrypt_string

        if self.encrypt_timestamp_key is not None:
            result['EncryptTimestampKey'] = self.encrypt_timestamp_key

        result['Headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['Headers'].append(k1.to_map() if k1 else None)

        if self.method is not None:
            result['Method'] = self.method

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('EncryptSignatureKey') is not None:
            self.encrypt_signature_key = m.get('EncryptSignatureKey')

        if m.get('EncryptString') is not None:
            self.encrypt_string = m.get('EncryptString')

        if m.get('EncryptTimestampKey') is not None:
            self.encrypt_timestamp_key = m.get('EncryptTimestampKey')

        self.headers = []
        if m.get('Headers') is not None:
            for k1 in m.get('Headers'):
                temp_model = main_models.PushingTargetHttpRequestTargetHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class PushingTargetHttpRequestTargetHeaders(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

