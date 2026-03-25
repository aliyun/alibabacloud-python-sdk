# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenAttachedChildInstancesResponseBody(DaraModel):
    def __init__(
        self,
        child_instances: main_models.DescribeCenAttachedChildInstancesResponseBodyChildInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.child_instances = child_instances
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.child_instances:
            self.child_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_instances is not None:
            result['ChildInstances'] = self.child_instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstances') is not None:
            temp_model = main_models.DescribeCenAttachedChildInstancesResponseBodyChildInstances()
            self.child_instances = temp_model.from_map(m.get('ChildInstances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenAttachedChildInstancesResponseBodyChildInstances(DaraModel):
    def __init__(
        self,
        child_instance: List[main_models.DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance] = None,
    ):
        self.child_instance = child_instance

    def validate(self):
        if self.child_instance:
            for v1 in self.child_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChildInstance'] = []
        if self.child_instance is not None:
            for k1 in self.child_instance:
                result['ChildInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_instance = []
        if m.get('ChildInstance') is not None:
            for k1 in m.get('ChildInstance'):
                temp_model = main_models.DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance()
                self.child_instance.append(temp_model.from_map(k1))

        return self

class DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        child_instance_attach_time: str = None,
        child_instance_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        managed_service: str = None,
        status: str = None,
    ):
        self.cen_id = cen_id
        self.child_instance_attach_time = child_instance_attach_time
        self.child_instance_id = child_instance_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_type = child_instance_type
        self.managed_service = managed_service
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time

        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id

        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id

        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type

        if self.managed_service is not None:
            result['ManagedService'] = self.managed_service

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')

        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')

        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')

        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')

        if m.get('ManagedService') is not None:
            self.managed_service = m.get('ManagedService')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

