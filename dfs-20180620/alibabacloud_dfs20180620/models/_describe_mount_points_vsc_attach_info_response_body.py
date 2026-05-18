# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dfs20180620 import models as main_models
from darabonba.model import DaraModel

class DescribeMountPointsVscAttachInfoResponseBody(DaraModel):
    def __init__(
        self,
        attach_infos: List[main_models.DescribeMountPointsVscAttachInfoResponseBodyAttachInfos] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.attach_infos = attach_infos
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.attach_infos:
            for v1 in self.attach_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachInfos'] = []
        if self.attach_infos is not None:
            for k1 in self.attach_infos:
                result['AttachInfos'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attach_infos = []
        if m.get('AttachInfos') is not None:
            for k1 in m.get('AttachInfos'):
                temp_model = main_models.DescribeMountPointsVscAttachInfoResponseBodyAttachInfos()
                self.attach_infos.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMountPointsVscAttachInfoResponseBodyAttachInfos(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mount_point_id: str = None,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_status: str = None,
        vsc_type: str = None,
    ):
        self.instance_id = instance_id
        self.mount_point_id = mount_point_id
        self.vsc_id = vsc_id
        self.vsc_name = vsc_name
        self.vsc_status = vsc_status
        self.vsc_type = vsc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name

        if self.vsc_status is not None:
            result['VscStatus'] = self.vsc_status

        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')

        if m.get('VscStatus') is not None:
            self.vsc_status = m.get('VscStatus')

        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')

        return self

