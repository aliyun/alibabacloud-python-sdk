# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceHAResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceHAResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceHAResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDBInstanceHAResponseBodyData(DaraModel):
    def __init__(
        self,
        primary_azone_id: str = None,
        primary_region_id: str = None,
        secondary_azone_id: str = None,
        secondary_region_id: str = None,
        topology_type: str = None,
    ):
        self.primary_azone_id = primary_azone_id
        self.primary_region_id = primary_region_id
        self.secondary_azone_id = secondary_azone_id
        self.secondary_region_id = secondary_region_id
        self.topology_type = topology_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary_azone_id is not None:
            result['PrimaryAzoneId'] = self.primary_azone_id

        if self.primary_region_id is not None:
            result['PrimaryRegionId'] = self.primary_region_id

        if self.secondary_azone_id is not None:
            result['SecondaryAzoneId'] = self.secondary_azone_id

        if self.secondary_region_id is not None:
            result['SecondaryRegionId'] = self.secondary_region_id

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimaryAzoneId') is not None:
            self.primary_azone_id = m.get('PrimaryAzoneId')

        if m.get('PrimaryRegionId') is not None:
            self.primary_region_id = m.get('PrimaryRegionId')

        if m.get('SecondaryAzoneId') is not None:
            self.secondary_azone_id = m.get('SecondaryAzoneId')

        if m.get('SecondaryRegionId') is not None:
            self.secondary_region_id = m.get('SecondaryRegionId')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        return self

