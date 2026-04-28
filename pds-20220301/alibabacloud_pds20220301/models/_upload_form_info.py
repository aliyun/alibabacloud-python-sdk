# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UploadFormInfo(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        form_data: Dict[str, str] = None,
        object_key: str = None,
        oss_access_key_id: str = None,
        oss_end_point: str = None,
        oss_security_token: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.form_data = form_data
        self.object_key = object_key
        self.oss_access_key_id = oss_access_key_id
        self.oss_end_point = oss_end_point
        self.oss_security_token = oss_security_token
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucket_name'] = self.bucket_name

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.form_data is not None:
            result['form_data'] = self.form_data

        if self.object_key is not None:
            result['object_key'] = self.object_key

        if self.oss_access_key_id is not None:
            result['oss_access_key_id'] = self.oss_access_key_id

        if self.oss_end_point is not None:
            result['oss_end_point'] = self.oss_end_point

        if self.oss_security_token is not None:
            result['oss_security_token'] = self.oss_security_token

        if self.policy is not None:
            result['policy'] = self.policy

        if self.signature is not None:
            result['signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket_name') is not None:
            self.bucket_name = m.get('bucket_name')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('form_data') is not None:
            self.form_data = m.get('form_data')

        if m.get('object_key') is not None:
            self.object_key = m.get('object_key')

        if m.get('oss_access_key_id') is not None:
            self.oss_access_key_id = m.get('oss_access_key_id')

        if m.get('oss_end_point') is not None:
            self.oss_end_point = m.get('oss_end_point')

        if m.get('oss_security_token') is not None:
            self.oss_security_token = m.get('oss_security_token')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        return self

