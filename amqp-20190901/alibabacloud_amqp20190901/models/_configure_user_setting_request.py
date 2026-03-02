# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureUserSettingRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        logstore: str = None,
        project_name: str = None,
        put_type: str = None,
    ):
        self.bucket_name = bucket_name
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.logstore = logstore
        self.project_name = project_name
        # This parameter is required.
        self.put_type = put_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.put_type is not None:
            result['PutType'] = self.put_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('PutType') is not None:
            self.put_type = m.get('PutType')

        return self

