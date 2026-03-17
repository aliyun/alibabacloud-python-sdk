# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeQosesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        qoses: main_models.DescribeQosesResponseBodyQoses = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        self.qoses = qoses
        # The ID of the request.
        self.request_id = request_id
        # The total number of QoS polices.
        self.total_count = total_count

    def validate(self):
        if self.qoses:
            self.qoses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.qoses is not None:
            result['Qoses'] = self.qoses.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Qoses') is not None:
            temp_model = main_models.DescribeQosesResponseBodyQoses()
            self.qoses = temp_model.from_map(m.get('Qoses'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeQosesResponseBodyQoses(DaraModel):
    def __init__(
        self,
        qos: List[main_models.DescribeQosesResponseBodyQosesQos] = None,
    ):
        self.qos = qos

    def validate(self):
        if self.qos:
            for v1 in self.qos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Qos'] = []
        if self.qos is not None:
            for k1 in self.qos:
                result['Qos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qos = []
        if m.get('Qos') is not None:
            for k1 in m.get('Qos'):
                temp_model = main_models.DescribeQosesResponseBodyQosesQos()
                self.qos.append(temp_model.from_map(k1))

        return self

class DescribeQosesResponseBodyQosesQos(DaraModel):
    def __init__(
        self,
        qos_description: str = None,
        qos_id: str = None,
        qos_name: str = None,
        resource_group_id: str = None,
        sag_count: str = None,
        smart_agids: str = None,
    ):
        self.qos_description = qos_description
        self.qos_id = qos_id
        self.qos_name = qos_name
        self.resource_group_id = resource_group_id
        self.sag_count = sag_count
        self.smart_agids = smart_agids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qos_description is not None:
            result['QosDescription'] = self.qos_description

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.qos_name is not None:
            result['QosName'] = self.qos_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sag_count is not None:
            result['SagCount'] = self.sag_count

        if self.smart_agids is not None:
            result['SmartAGIds'] = self.smart_agids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QosDescription') is not None:
            self.qos_description = m.get('QosDescription')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QosName') is not None:
            self.qos_name = m.get('QosName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SagCount') is not None:
            self.sag_count = m.get('SagCount')

        if m.get('SmartAGIds') is not None:
            self.smart_agids = m.get('SmartAGIds')

        return self

