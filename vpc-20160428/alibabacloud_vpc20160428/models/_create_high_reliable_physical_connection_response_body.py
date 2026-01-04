# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateHighReliablePhysicalConnectionResponseBody(DaraModel):
    def __init__(
        self,
        error_info_list: main_models.CreateHighReliablePhysicalConnectionResponseBodyErrorInfoList = None,
        physical_connection_list: main_models.CreateHighReliablePhysicalConnectionResponseBodyPhysicalConnectionList = None,
        request_id: str = None,
    ):
        # If the request fails the dry run, the following error codes and error messages may be returned:
        # 
        # - pconn.high.reliable.dryrun.error.disable.outbound.data.transfer.billing. Billing for outbound data transfer is not enabled.
        # - pconn.high.reliable.dryrun.error.incompatable.device.capacity. No device in the access point supports advanced features.
        # - pconn.high.reliable.dryrun.error.quota.exceeded. The quota is insufficient.
        # - pconn.high.reliable.dryrun.error.not.enough.resource. The access point resources are insufficient.
        self.error_info_list = error_info_list
        # The Express Connect circuits.
        self.physical_connection_list = physical_connection_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.error_info_list:
            self.error_info_list.validate()
        if self.physical_connection_list:
            self.physical_connection_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_info_list is not None:
            result['ErrorInfoList'] = self.error_info_list.to_map()

        if self.physical_connection_list is not None:
            result['PhysicalConnectionList'] = self.physical_connection_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorInfoList') is not None:
            temp_model = main_models.CreateHighReliablePhysicalConnectionResponseBodyErrorInfoList()
            self.error_info_list = temp_model.from_map(m.get('ErrorInfoList'))

        if m.get('PhysicalConnectionList') is not None:
            temp_model = main_models.CreateHighReliablePhysicalConnectionResponseBodyPhysicalConnectionList()
            self.physical_connection_list = temp_model.from_map(m.get('PhysicalConnectionList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateHighReliablePhysicalConnectionResponseBodyPhysicalConnectionList(DaraModel):
    def __init__(
        self,
        physical_connection_list: List[main_models.CreateHighReliablePhysicalConnectionResponseBodyPhysicalConnectionListPhysicalConnectionList] = None,
    ):
        self.physical_connection_list = physical_connection_list

    def validate(self):
        if self.physical_connection_list:
            for v1 in self.physical_connection_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['physicalConnectionList'] = []
        if self.physical_connection_list is not None:
            for k1 in self.physical_connection_list:
                result['physicalConnectionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.physical_connection_list = []
        if m.get('physicalConnectionList') is not None:
            for k1 in m.get('physicalConnectionList'):
                temp_model = main_models.CreateHighReliablePhysicalConnectionResponseBodyPhysicalConnectionListPhysicalConnectionList()
                self.physical_connection_list.append(temp_model.from_map(k1))

        return self

class CreateHighReliablePhysicalConnectionResponseBodyPhysicalConnectionListPhysicalConnectionList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_no: str = None,
    ):
        # The ID of the Express Connect circuit.
        self.instance_id = instance_id
        # The region ID of the Express Connect circuit.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

class CreateHighReliablePhysicalConnectionResponseBodyErrorInfoList(DaraModel):
    def __init__(
        self,
        error_info_list: List[main_models.CreateHighReliablePhysicalConnectionResponseBodyErrorInfoListErrorInfoList] = None,
    ):
        self.error_info_list = error_info_list

    def validate(self):
        if self.error_info_list:
            for v1 in self.error_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['errorInfoList'] = []
        if self.error_info_list is not None:
            for k1 in self.error_info_list:
                result['errorInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_info_list = []
        if m.get('errorInfoList') is not None:
            for k1 in m.get('errorInfoList'):
                temp_model = main_models.CreateHighReliablePhysicalConnectionResponseBodyErrorInfoListErrorInfoList()
                self.error_info_list.append(temp_model.from_map(k1))

        return self

class CreateHighReliablePhysicalConnectionResponseBodyErrorInfoListErrorInfoList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance_id: str = None,
    ):
        # Error codes.
        self.error_code = error_code
        # The returned error message.
        self.error_message = error_message
        # The ID of the Express Connect circuit.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

