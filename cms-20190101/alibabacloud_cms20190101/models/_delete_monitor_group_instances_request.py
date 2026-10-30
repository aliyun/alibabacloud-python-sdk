# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMonitorGroupInstancesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        dry_run: bool = None,
        group_id: int = None,
        instance_id_list: str = None,
        region_id: str = None,
    ):
        # The abbreviation of the cloud service name.
        # 
        # > For more information about how to obtain the abbreviation of a cloud service name, see the `metricCategory` field in the `Labels` response parameter of the [DescribeProjectMeta](https://help.aliyun.com/document_detail/114916.html) operation.
        # 
        # This parameter is required.
        self.category = category
        # Specifies whether to perform only a dry run on the request. Valid values:
        # - **true**: performs a dry run. The system checks the required parameters, request format, and service limits, but does not delete the instances. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a normal request. If the request passes the check, the instances are deleted.
        self.dry_run = dry_run
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The IDs of the instances to be deleted. Separate multiple instance IDs with commas (,). You can delete up to 20 instances at a time.
        # 
        # This parameter is required.
        self.instance_id_list = instance_id_list
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

