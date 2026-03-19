# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceDetailsResponseBody(DaraModel):
    def __init__(
        self,
        instance_details: List[main_models.DescribeInstanceDetailsResponseBodyInstanceDetails] = None,
        request_id: str = None,
    ):
        self.instance_details = instance_details
        self.request_id = request_id

    def validate(self):
        if self.instance_details:
            for v1 in self.instance_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k1 in self.instance_details:
                result['InstanceDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k1 in m.get('InstanceDetails'):
                temp_model = main_models.DescribeInstanceDetailsResponseBodyInstanceDetails()
                self.instance_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceDetailsResponseBodyInstanceDetails(DaraModel):
    def __init__(
        self,
        eip_info_list: List[main_models.DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfoList] = None,
        instance_id: str = None,
        line: str = None,
    ):
        self.eip_info_list = eip_info_list
        self.instance_id = instance_id
        self.line = line

    def validate(self):
        if self.eip_info_list:
            for v1 in self.eip_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipInfoList'] = []
        if self.eip_info_list is not None:
            for k1 in self.eip_info_list:
                result['EipInfoList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_info_list = []
        if m.get('EipInfoList') is not None:
            for k1 in m.get('EipInfoList'):
                temp_model = main_models.DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfoList()
                self.eip_info_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

class DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfoList(DaraModel):
    def __init__(
        self,
        eip: str = None,
        status: str = None,
    ):
        self.eip = eip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip is not None:
            result['Eip'] = self.eip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

