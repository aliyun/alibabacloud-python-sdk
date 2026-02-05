# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobDataUploadParamsRequest(DaraModel):
    def __init__(
        self,
        busi_type: str = None,
        file_name: str = None,
        instance_id: str = None,
        path: str = None,
        unique_id: str = None,
    ):
        self.busi_type = busi_type
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.instance_id = instance_id
        self.path = path
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.busi_type is not None:
            result['BusiType'] = self.busi_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.path is not None:
            result['Path'] = self.path

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusiType') is not None:
            self.busi_type = m.get('BusiType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        return self

