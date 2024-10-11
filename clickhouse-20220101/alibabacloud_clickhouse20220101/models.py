# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocateVirtualWareHousePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class AllocateVirtualWareHousePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateVirtualWareHousePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateVirtualWareHousePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AllocateVirtualWareHousePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCreateClusterRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        dbcluster_description: str = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        used_time: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.dbcluster_description = dbcluster_description
        # This parameter is required.
        self.pay_type = pay_type
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        self.used_time = used_time
        # This parameter is required.
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        # This parameter is required.
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.vswitch_id = vswitch_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckCreateClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        expected_dbcluster_status: str = None,
        expected_order_finish_seconds: int = None,
        expected_target_virtual_ware_house_status: str = None,
    ):
        self.expected_dbcluster_status = expected_dbcluster_status
        self.expected_order_finish_seconds = expected_order_finish_seconds
        self.expected_target_virtual_ware_house_status = expected_target_virtual_ware_house_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expected_dbcluster_status is not None:
            result['ExpectedDBClusterStatus'] = self.expected_dbcluster_status
        if self.expected_order_finish_seconds is not None:
            result['ExpectedOrderFinishSeconds'] = self.expected_order_finish_seconds
        if self.expected_target_virtual_ware_house_status is not None:
            result['ExpectedTargetVirtualWareHouseStatus'] = self.expected_target_virtual_ware_house_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedDBClusterStatus') is not None:
            self.expected_dbcluster_status = m.get('ExpectedDBClusterStatus')
        if m.get('ExpectedOrderFinishSeconds') is not None:
            self.expected_order_finish_seconds = m.get('ExpectedOrderFinishSeconds')
        if m.get('ExpectedTargetVirtualWareHouseStatus') is not None:
            self.expected_target_virtual_ware_house_status = m.get('ExpectedTargetVirtualWareHouseStatus')
        return self


class CheckCreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckCreateClusterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckCreateClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckCreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckCreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckCreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCreateVirtualWareHouseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        # This parameter is required.
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckCreateVirtualWareHouseResponseBodyData(TeaModel):
    def __init__(
        self,
        expected_dbcluster_status: str = None,
        expected_order_finish_seconds: int = None,
        expected_target_virtual_ware_house_status: str = None,
    ):
        self.expected_dbcluster_status = expected_dbcluster_status
        self.expected_order_finish_seconds = expected_order_finish_seconds
        self.expected_target_virtual_ware_house_status = expected_target_virtual_ware_house_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expected_dbcluster_status is not None:
            result['ExpectedDBClusterStatus'] = self.expected_dbcluster_status
        if self.expected_order_finish_seconds is not None:
            result['ExpectedOrderFinishSeconds'] = self.expected_order_finish_seconds
        if self.expected_target_virtual_ware_house_status is not None:
            result['ExpectedTargetVirtualWareHouseStatus'] = self.expected_target_virtual_ware_house_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedDBClusterStatus') is not None:
            self.expected_dbcluster_status = m.get('ExpectedDBClusterStatus')
        if m.get('ExpectedOrderFinishSeconds') is not None:
            self.expected_order_finish_seconds = m.get('ExpectedOrderFinishSeconds')
        if m.get('ExpectedTargetVirtualWareHouseStatus') is not None:
            self.expected_target_virtual_ware_house_status = m.get('ExpectedTargetVirtualWareHouseStatus')
        return self


class CheckCreateVirtualWareHouseResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckCreateVirtualWareHouseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckCreateVirtualWareHouseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckCreateVirtualWareHouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckCreateVirtualWareHouseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckCreateVirtualWareHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDeleteVirtualWareHouseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class CheckDeleteVirtualWareHouseResponseBodyData(TeaModel):
    def __init__(
        self,
        expected_dbcluster_status: str = None,
        expected_order_finish_seconds: int = None,
        expected_target_virtual_ware_house_status: str = None,
    ):
        self.expected_dbcluster_status = expected_dbcluster_status
        self.expected_order_finish_seconds = expected_order_finish_seconds
        self.expected_target_virtual_ware_house_status = expected_target_virtual_ware_house_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expected_dbcluster_status is not None:
            result['ExpectedDBClusterStatus'] = self.expected_dbcluster_status
        if self.expected_order_finish_seconds is not None:
            result['ExpectedOrderFinishSeconds'] = self.expected_order_finish_seconds
        if self.expected_target_virtual_ware_house_status is not None:
            result['ExpectedTargetVirtualWareHouseStatus'] = self.expected_target_virtual_ware_house_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedDBClusterStatus') is not None:
            self.expected_dbcluster_status = m.get('ExpectedDBClusterStatus')
        if m.get('ExpectedOrderFinishSeconds') is not None:
            self.expected_order_finish_seconds = m.get('ExpectedOrderFinishSeconds')
        if m.get('ExpectedTargetVirtualWareHouseStatus') is not None:
            self.expected_target_virtual_ware_house_status = m.get('ExpectedTargetVirtualWareHouseStatus')
        return self


class CheckDeleteVirtualWareHouseResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckDeleteVirtualWareHouseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckDeleteVirtualWareHouseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDeleteVirtualWareHouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDeleteVirtualWareHouseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckDeleteVirtualWareHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckModifyVirtualWareHouseResourceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        # This parameter is required.
        self.virtual_ware_house_class = virtual_ware_house_class
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class CheckModifyVirtualWareHouseResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        expected_dbcluster_status: str = None,
        expected_order_finish_seconds: int = None,
        expected_target_virtual_ware_house_status: str = None,
    ):
        self.expected_dbcluster_status = expected_dbcluster_status
        self.expected_order_finish_seconds = expected_order_finish_seconds
        self.expected_target_virtual_ware_house_status = expected_target_virtual_ware_house_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expected_dbcluster_status is not None:
            result['ExpectedDBClusterStatus'] = self.expected_dbcluster_status
        if self.expected_order_finish_seconds is not None:
            result['ExpectedOrderFinishSeconds'] = self.expected_order_finish_seconds
        if self.expected_target_virtual_ware_house_status is not None:
            result['ExpectedTargetVirtualWareHouseStatus'] = self.expected_target_virtual_ware_house_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedDBClusterStatus') is not None:
            self.expected_dbcluster_status = m.get('ExpectedDBClusterStatus')
        if m.get('ExpectedOrderFinishSeconds') is not None:
            self.expected_order_finish_seconds = m.get('ExpectedOrderFinishSeconds')
        if m.get('ExpectedTargetVirtualWareHouseStatus') is not None:
            self.expected_target_virtual_ware_house_status = m.get('ExpectedTargetVirtualWareHouseStatus')
        return self


class CheckModifyVirtualWareHouseResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckModifyVirtualWareHouseResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckModifyVirtualWareHouseResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckModifyVirtualWareHouseResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckModifyVirtualWareHouseResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckModifyVirtualWareHouseResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        comment: str = None,
        dbcluster_id: str = None,
        password: str = None,
        password_sha_256hex: str = None,
        privilege_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        self.comment = comment
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.password = password
        self.password_sha_256hex = password_sha_256hex
        # This parameter is required.
        self.privilege_type = privilege_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.password is not None:
            result['Password'] = self.password
        if self.password_sha_256hex is not None:
            result['PasswordSha256Hex'] = self.password_sha_256hex
        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordSha256Hex') is not None:
            self.password_sha_256hex = m.get('PasswordSha256Hex')
        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        dbcluster_description: str = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        used_time: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.dbcluster_description = dbcluster_description
        # This parameter is required.
        self.pay_type = pay_type
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        self.used_time = used_time
        # This parameter is required.
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        # This parameter is required.
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.vswitch_id = vswitch_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        order_id: int = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.order_id = order_id
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateClusterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualWareHouseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        # This parameter is required.
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVirtualWareHouseResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        virtual_ware_house_id: str = None,
    ):
        self.order_id = order_id
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class CreateVirtualWareHouseResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateVirtualWareHouseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateVirtualWareHouseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVirtualWareHouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVirtualWareHouseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVirtualWareHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteClusterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterSecurityIPGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteClusterSecurityIPGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterSecurityIPGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterSecurityIPGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualWareHouseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class DeleteVirtualWareHouseResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteVirtualWareHouseResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteVirtualWareHouseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteVirtualWareHouseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVirtualWareHouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVirtualWareHouseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVirtualWareHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        comment: str = None,
        password_sha_256hex: str = None,
        privilege_description: str = None,
        privilege_type: str = None,
    ):
        self.account = account
        self.comment = comment
        self.password_sha_256hex = password_sha_256hex
        self.privilege_description = privilege_description
        self.privilege_type = privilege_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.password_sha_256hex is not None:
            result['PasswordSha256Hex'] = self.password_sha_256hex
        if self.privilege_description is not None:
            result['PrivilegeDescription'] = self.privilege_description
        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PasswordSha256Hex') is not None:
            self.password_sha_256hex = m.get('PasswordSha256Hex')
        if m.get('PrivilegeDescription') is not None:
            self.privilege_description = m.get('PrivilegeDescription')
        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')
        return self


class DescribeAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAccountResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeClusterResponseBodyDataVirtualWareHouses(TeaModel):
    def __init__(
        self,
        ports: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        virtual_ware_house_id: str = None,
        virtual_ware_house_status: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ports = ports
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        self.virtual_ware_house_id = virtual_ware_house_id
        self.virtual_ware_house_status = virtual_ware_house_status
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        if self.virtual_ware_house_status is not None:
            result['VirtualWareHouseStatus'] = self.virtual_ware_house_status
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        if m.get('VirtualWareHouseStatus') is not None:
            self.virtual_ware_house_status = m.get('VirtualWareHouseStatus')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cache_storage_size_gi_b: int = None,
        cache_storage_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        engine_version: str = None,
        expire_time: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        object_store_size_gi_b: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_cpu_cores: int = None,
        resource_memory_gi_b: int = None,
        virtual_ware_houses: List[DescribeClusterResponseBodyDataVirtualWareHouses] = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.cache_storage_size_gi_b = cache_storage_size_gi_b
        self.cache_storage_type = cache_storage_type
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_status = dbcluster_status
        self.engine_version = engine_version
        self.expire_time = expire_time
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.object_store_size_gi_b = object_store_size_gi_b
        self.pay_type = pay_type
        self.region_id = region_id
        self.resource_cpu_cores = resource_cpu_cores
        self.resource_memory_gi_b = resource_memory_gi_b
        self.virtual_ware_houses = virtual_ware_houses
        # VPC ID。
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        if self.virtual_ware_houses:
            for k in self.virtual_ware_houses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cache_storage_size_gi_b is not None:
            result['CacheStorageSizeGiB'] = self.cache_storage_size_gi_b
        if self.cache_storage_type is not None:
            result['CacheStorageType'] = self.cache_storage_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.object_store_size_gi_b is not None:
            result['ObjectStoreSizeGiB'] = self.object_store_size_gi_b
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_cpu_cores is not None:
            result['ResourceCpuCores'] = self.resource_cpu_cores
        if self.resource_memory_gi_b is not None:
            result['ResourceMemoryGiB'] = self.resource_memory_gi_b
        result['VirtualWareHouses'] = []
        if self.virtual_ware_houses is not None:
            for k in self.virtual_ware_houses:
                result['VirtualWareHouses'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CacheStorageSizeGiB') is not None:
            self.cache_storage_size_gi_b = m.get('CacheStorageSizeGiB')
        if m.get('CacheStorageType') is not None:
            self.cache_storage_type = m.get('CacheStorageType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('ObjectStoreSizeGiB') is not None:
            self.object_store_size_gi_b = m.get('ObjectStoreSizeGiB')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceCpuCores') is not None:
            self.resource_cpu_cores = m.get('ResourceCpuCores')
        if m.get('ResourceMemoryGiB') is not None:
            self.resource_memory_gi_b = m.get('ResourceMemoryGiB')
        self.virtual_ware_houses = []
        if m.get('VirtualWareHouses') is not None:
            for k in m.get('VirtualWareHouses'):
                temp_model = DescribeClusterResponseBodyDataVirtualWareHouses()
                self.virtual_ware_houses.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeClusterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterSecurityInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeClusterSecurityInfoResponseBodyDataSecurityIpGroups(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        security_ips: str = None,
    ):
        self.group_name = group_name
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class DescribeClusterSecurityInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        security_ip_groups: List[DescribeClusterSecurityInfoResponseBodyDataSecurityIpGroups] = None,
    ):
        self.security_ip_groups = security_ip_groups

    def validate(self):
        if self.security_ip_groups:
            for k in self.security_ip_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecurityIpGroups'] = []
        if self.security_ip_groups is not None:
            for k in self.security_ip_groups:
                result['SecurityIpGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_ip_groups = []
        if m.get('SecurityIpGroups') is not None:
            for k in m.get('SecurityIpGroups'):
                temp_model = DescribeClusterSecurityInfoResponseBodyDataSecurityIpGroups()
                self.security_ip_groups.append(temp_model.from_map(k))
        return self


class DescribeClusterSecurityInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeClusterSecurityInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeClusterSecurityInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterSecurityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterSecurityInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterSecurityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterStatusSetResponseBodyData(TeaModel):
    def __init__(
        self,
        desc: str = None,
        value: str = None,
    ):
        self.desc = desc
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeClusterStatusSetResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeClusterStatusSetResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeClusterStatusSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterStatusSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterStatusSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterStatusSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyDataZones(TeaModel):
    def __init__(
        self,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        self.vpc_enabled = vpc_enabled
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyData(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zones: List[DescribeRegionsResponseBodyDataZones] = None,
    ):
        self.region_id = region_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeRegionsResponseBodyDataZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeRegionsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRunningQueryRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        query_duration_ms: int = None,
        query_id: str = None,
        query_key_word: str = None,
        query_user: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.query_duration_ms = query_duration_ms
        self.query_id = query_id
        self.query_key_word = query_key_word
        self.query_user = query_user
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.query_key_word is not None:
            result['QueryKeyWord'] = self.query_key_word
        if self.query_user is not None:
            result['QueryUser'] = self.query_user
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('QueryKeyWord') is not None:
            self.query_key_word = m.get('QueryKeyWord')
        if m.get('QueryUser') is not None:
            self.query_user = m.get('QueryUser')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class DescribeRunningQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        query: str = None,
        query_duration_ms: int = None,
        query_start_time: str = None,
    ):
        self.initial_address = initial_address
        self.initial_query_id = initial_query_id
        self.initial_user = initial_user
        self.query = query
        self.query_duration_ms = query_duration_ms
        self.query_start_time = query_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.query is not None:
            result['Query'] = self.query
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        return self


class DescribeRunningQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeRunningQueryResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeRunningQueryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRunningQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRunningQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRunningQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowQueryRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        query_duration_ms: int = None,
        region_id: str = None,
        start_time: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.query_duration_ms = query_duration_ms
        self.region_id = region_id
        self.start_time = start_time
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class DescribeSlowQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        initial_address: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        memory_usage: int = None,
        query: str = None,
        query_duration_ms: int = None,
        query_start_time: str = None,
        query_state: str = None,
        read_bytes: int = None,
        read_rows: int = None,
        result_bytes: int = None,
        result_rows: int = None,
    ):
        self.initial_address = initial_address
        self.initial_query_id = initial_query_id
        self.initial_user = initial_user
        self.memory_usage = memory_usage
        self.query = query
        self.query_duration_ms = query_duration_ms
        self.query_start_time = query_start_time
        self.query_state = query_state
        self.read_bytes = read_bytes
        self.read_rows = read_rows
        self.result_bytes = result_bytes
        self.result_rows = result_rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_address is not None:
            result['InitialAddress'] = self.initial_address
        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id
        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user
        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage
        if self.query is not None:
            result['Query'] = self.query
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        if self.query_state is not None:
            result['QueryState'] = self.query_state
        if self.read_bytes is not None:
            result['ReadBytes'] = self.read_bytes
        if self.read_rows is not None:
            result['ReadRows'] = self.read_rows
        if self.result_bytes is not None:
            result['ResultBytes'] = self.result_bytes
        if self.result_rows is not None:
            result['ResultRows'] = self.result_rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialAddress') is not None:
            self.initial_address = m.get('InitialAddress')
        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')
        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')
        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        if m.get('QueryState') is not None:
            self.query_state = m.get('QueryState')
        if m.get('ReadBytes') is not None:
            self.read_bytes = m.get('ReadBytes')
        if m.get('ReadRows') is not None:
            self.read_rows = m.get('ReadRows')
        if m.get('ResultBytes') is not None:
            self.result_bytes = m.get('ResultBytes')
        if m.get('ResultRows') is not None:
            self.result_rows = m.get('ResultRows')
        return self


class DescribeSlowQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeSlowQueryResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeSlowQueryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSlowQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowQueryTrendRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        query_duration_ms: int = None,
        region_id: str = None,
        start_time: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.end_time = end_time
        self.query_duration_ms = query_duration_ms
        self.region_id = region_id
        self.start_time = start_time
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class DescribeSlowQueryTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        avg_duration_ms: int = None,
        count: int = None,
        max_duration_ms: int = None,
        min_duration_ms: int = None,
        start_time: str = None,
    ):
        self.avg_duration_ms = avg_duration_ms
        self.count = count
        self.max_duration_ms = max_duration_ms
        self.min_duration_ms = min_duration_ms
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_duration_ms is not None:
            result['AvgDurationMs'] = self.avg_duration_ms
        if self.count is not None:
            result['Count'] = self.count
        if self.max_duration_ms is not None:
            result['MaxDurationMs'] = self.max_duration_ms
        if self.min_duration_ms is not None:
            result['MinDurationMs'] = self.min_duration_ms
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgDurationMs') is not None:
            self.avg_duration_ms = m.get('AvgDurationMs')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('MaxDurationMs') is not None:
            self.max_duration_ms = m.get('MaxDurationMs')
        if m.get('MinDurationMs') is not None:
            self.min_duration_ms = m.get('MinDurationMs')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeSlowQueryTrendResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeSlowQueryTrendResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeSlowQueryTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlowQueryTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowQueryTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlowQueryTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualWareHouseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class DescribeVirtualWareHouseResponseBodyData(TeaModel):
    def __init__(
        self,
        ports: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        virtual_ware_house_id: str = None,
        virtual_ware_house_status: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ports = ports
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        self.virtual_ware_house_id = virtual_ware_house_id
        self.virtual_ware_house_status = virtual_ware_house_status
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        if self.virtual_ware_house_status is not None:
            result['VirtualWareHouseStatus'] = self.virtual_ware_house_status
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        if m.get('VirtualWareHouseStatus') is not None:
            self.virtual_ware_house_status = m.get('VirtualWareHouseStatus')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVirtualWareHouseResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeVirtualWareHouseResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeVirtualWareHouseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVirtualWareHouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVirtualWareHouseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVirtualWareHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualWareHouseClassSetResponseBodyData(TeaModel):
    def __init__(
        self,
        cache_storage_step: int = None,
        cpu_cores: int = None,
        max_cache_storage: int = None,
        memory_gi_b: int = None,
        min_cache_storage: int = None,
        value: str = None,
    ):
        self.cache_storage_step = cache_storage_step
        self.cpu_cores = cpu_cores
        self.max_cache_storage = max_cache_storage
        self.memory_gi_b = memory_gi_b
        self.min_cache_storage = min_cache_storage
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_storage_step is not None:
            result['CacheStorageStep'] = self.cache_storage_step
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.max_cache_storage is not None:
            result['MaxCacheStorage'] = self.max_cache_storage
        if self.memory_gi_b is not None:
            result['MemoryGiB'] = self.memory_gi_b
        if self.min_cache_storage is not None:
            result['MinCacheStorage'] = self.min_cache_storage
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheStorageStep') is not None:
            self.cache_storage_step = m.get('CacheStorageStep')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('MaxCacheStorage') is not None:
            self.max_cache_storage = m.get('MaxCacheStorage')
        if m.get('MemoryGiB') is not None:
            self.memory_gi_b = m.get('MemoryGiB')
        if m.get('MinCacheStorage') is not None:
            self.min_cache_storage = m.get('MinCacheStorage')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVirtualWareHouseClassSetResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeVirtualWareHouseClassSetResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeVirtualWareHouseClassSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVirtualWareHouseClassSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVirtualWareHouseClassSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVirtualWareHouseClassSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualWareHouseEndpointInfoRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class DescribeVirtualWareHouseEndpointInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
        ip: str = None,
        net_type: str = None,
        ports: str = None,
        status: str = None,
        url: str = None,
    ):
        self.endpoint_type = endpoint_type
        self.ip = ip
        self.net_type = net_type
        self.ports = ports
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeVirtualWareHouseEndpointInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeVirtualWareHouseEndpointInfoResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeVirtualWareHouseEndpointInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVirtualWareHouseEndpointInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVirtualWareHouseEndpointInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVirtualWareHouseEndpointInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualWareHouseStatusSetResponseBodyData(TeaModel):
    def __init__(
        self,
        desc: str = None,
        value: str = None,
    ):
        self.desc = desc
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVirtualWareHouseStatusSetResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeVirtualWareHouseStatusSetResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeVirtualWareHouseStatusSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVirtualWareHouseStatusSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVirtualWareHouseStatusSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVirtualWareHouseStatusSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDistributedTablesBufferSizeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class GetDistributedTablesBufferSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        buffer_size_gi_b: int = None,
    ):
        self.buffer_size_gi_b = buffer_size_gi_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buffer_size_gi_b is not None:
            result['BufferSizeGiB'] = self.buffer_size_gi_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BufferSizeGiB') is not None:
            self.buffer_size_gi_b = m.get('BufferSizeGiB')
        return self


class GetDistributedTablesBufferSizeResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDistributedTablesBufferSizeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDistributedTablesBufferSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDistributedTablesBufferSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDistributedTablesBufferSizeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDistributedTablesBufferSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillQueryRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        query_ids: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.query_ids = query_ids
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.query_ids is not None:
            result['QueryIds'] = self.query_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('QueryIds') is not None:
            self.query_ids = m.get('QueryIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class KillQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = KillQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccountsResponseBodyData(TeaModel):
    def __init__(
        self,
        account: str = None,
        comment: str = None,
        password_sha_256hex: str = None,
        privilege_description: str = None,
        privilege_type: str = None,
    ):
        self.account = account
        self.comment = comment
        self.password_sha_256hex = password_sha_256hex
        self.privilege_description = privilege_description
        self.privilege_type = privilege_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.password_sha_256hex is not None:
            result['PasswordSha256Hex'] = self.password_sha_256hex
        if self.privilege_description is not None:
            result['PrivilegeDescription'] = self.privilege_description
        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PasswordSha256Hex') is not None:
            self.password_sha_256hex = m.get('PasswordSha256Hex')
        if m.get('PrivilegeDescription') is not None:
            self.privilege_description = m.get('PrivilegeDescription')
        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')
        return self


class ListAccountsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAccountsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccountsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_status = dbcluster_status
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClustersResponseBodyDataVirtualWareHouses(TeaModel):
    def __init__(
        self,
        ports: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        virtual_ware_house_id: str = None,
        virtual_ware_house_status: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ports = ports
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        self.virtual_ware_house_id = virtual_ware_house_id
        self.virtual_ware_house_status = virtual_ware_house_status
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        if self.virtual_ware_house_status is not None:
            result['VirtualWareHouseStatus'] = self.virtual_ware_house_status
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        if m.get('VirtualWareHouseStatus') is not None:
            self.virtual_ware_house_status = m.get('VirtualWareHouseStatus')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        cache_storage_size_gi_b: int = None,
        cache_storage_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbcluster_status: str = None,
        engine_version: str = None,
        expire_time: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        object_store_size_gi_b: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_cpu_cores: int = None,
        resource_memory_gi_b: int = None,
        virtual_ware_houses: List[ListClustersResponseBodyDataVirtualWareHouses] = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.cache_storage_size_gi_b = cache_storage_size_gi_b
        self.cache_storage_type = cache_storage_type
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.dbcluster_description = dbcluster_description
        self.dbcluster_id = dbcluster_id
        self.dbcluster_status = dbcluster_status
        self.engine_version = engine_version
        self.expire_time = expire_time
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.object_store_size_gi_b = object_store_size_gi_b
        self.pay_type = pay_type
        self.region_id = region_id
        self.resource_cpu_cores = resource_cpu_cores
        self.resource_memory_gi_b = resource_memory_gi_b
        self.virtual_ware_houses = virtual_ware_houses
        # VPC ID。
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        if self.virtual_ware_houses:
            for k in self.virtual_ware_houses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.cache_storage_size_gi_b is not None:
            result['CacheStorageSizeGiB'] = self.cache_storage_size_gi_b
        if self.cache_storage_type is not None:
            result['CacheStorageType'] = self.cache_storage_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbcluster_status is not None:
            result['DBClusterStatus'] = self.dbcluster_status
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.object_store_size_gi_b is not None:
            result['ObjectStoreSizeGiB'] = self.object_store_size_gi_b
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_cpu_cores is not None:
            result['ResourceCpuCores'] = self.resource_cpu_cores
        if self.resource_memory_gi_b is not None:
            result['ResourceMemoryGiB'] = self.resource_memory_gi_b
        result['VirtualWareHouses'] = []
        if self.virtual_ware_houses is not None:
            for k in self.virtual_ware_houses:
                result['VirtualWareHouses'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CacheStorageSizeGiB') is not None:
            self.cache_storage_size_gi_b = m.get('CacheStorageSizeGiB')
        if m.get('CacheStorageType') is not None:
            self.cache_storage_type = m.get('CacheStorageType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBClusterStatus') is not None:
            self.dbcluster_status = m.get('DBClusterStatus')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('ObjectStoreSizeGiB') is not None:
            self.object_store_size_gi_b = m.get('ObjectStoreSizeGiB')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceCpuCores') is not None:
            self.resource_cpu_cores = m.get('ResourceCpuCores')
        if m.get('ResourceMemoryGiB') is not None:
            self.resource_memory_gi_b = m.get('ResourceMemoryGiB')
        self.virtual_ware_houses = []
        if m.get('VirtualWareHouses') is not None:
            for k in m.get('VirtualWareHouses'):
                temp_model = ListClustersResponseBodyDataVirtualWareHouses()
                self.virtual_ware_houses.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListClustersResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualWareHouseConfigsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class ListVirtualWareHouseConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        config_full_path: str = None,
        config_type: str = None,
        default_value: str = None,
        description: str = None,
        need_restart: bool = None,
        spec: str = None,
        value: str = None,
    ):
        self.config_full_path = config_full_path
        self.config_type = config_type
        self.default_value = default_value
        self.description = description
        self.need_restart = need_restart
        self.spec = spec
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_full_path is not None:
            result['ConfigFullPath'] = self.config_full_path
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFullPath') is not None:
            self.config_full_path = m.get('ConfigFullPath')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListVirtualWareHouseConfigsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListVirtualWareHouseConfigsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVirtualWareHouseConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVirtualWareHouseConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVirtualWareHouseConfigsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVirtualWareHouseConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualWareHousesRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVirtualWareHousesResponseBodyData(TeaModel):
    def __init__(
        self,
        ports: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_description: str = None,
        virtual_ware_house_id: str = None,
        virtual_ware_house_status: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ports = ports
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        self.virtual_ware_house_class = virtual_ware_house_class
        self.virtual_ware_house_description = virtual_ware_house_description
        self.virtual_ware_house_id = virtual_ware_house_id
        self.virtual_ware_house_status = virtual_ware_house_status
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        if self.virtual_ware_house_status is not None:
            result['VirtualWareHouseStatus'] = self.virtual_ware_house_status
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        if m.get('VirtualWareHouseStatus') is not None:
            self.virtual_ware_house_status = m.get('VirtualWareHouseStatus')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVirtualWareHousesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListVirtualWareHousesResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVirtualWareHousesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVirtualWareHousesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVirtualWareHousesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVirtualWareHousesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        comment: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountPrivilegeRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbcluster_id: str = None,
        privilege_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.privilege_type = privilege_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountPrivilegeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAccountPrivilegeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountPrivilegeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccountPrivilegeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_description = dbcluster_description
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyClusterDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyClusterDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVirtualWareHouseConfigRequestConfigChanges(TeaModel):
    def __init__(
        self,
        config_full_path: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.config_full_path = config_full_path
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_full_path is not None:
            result['ConfigFullPath'] = self.config_full_path
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFullPath') is not None:
            self.config_full_path = m.get('ConfigFullPath')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyVirtualWareHouseConfigRequest(TeaModel):
    def __init__(
        self,
        config_changes: List[ModifyVirtualWareHouseConfigRequestConfigChanges] = None,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        # This parameter is required.
        self.config_changes = config_changes
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        if self.config_changes:
            for k in self.config_changes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigChanges'] = []
        if self.config_changes is not None:
            for k in self.config_changes:
                result['ConfigChanges'].append(k.to_map() if k else None)
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_changes = []
        if m.get('ConfigChanges') is not None:
            for k in m.get('ConfigChanges'):
                temp_model = ModifyVirtualWareHouseConfigRequestConfigChanges()
                self.config_changes.append(temp_model.from_map(k))
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class ModifyVirtualWareHouseConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        config_changes_shrink: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        # This parameter is required.
        self.config_changes_shrink = config_changes_shrink
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_changes_shrink is not None:
            result['ConfigChanges'] = self.config_changes_shrink
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigChanges') is not None:
            self.config_changes_shrink = m.get('ConfigChanges')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class ModifyVirtualWareHouseConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVirtualWareHouseConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVirtualWareHouseConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVirtualWareHouseConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVirtualWareHouseDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_description: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_description = virtual_ware_house_description
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_description is not None:
            result['VirtualWareHouseDescription'] = self.virtual_ware_house_description
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseDescription') is not None:
            self.virtual_ware_house_description = m.get('VirtualWareHouseDescription')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class ModifyVirtualWareHouseDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVirtualWareHouseDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVirtualWareHouseDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVirtualWareHouseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVirtualWareHouseResourceRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_cache_storage: int = None,
        virtual_ware_house_class: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_cache_storage = virtual_ware_house_cache_storage
        # This parameter is required.
        self.virtual_ware_house_class = virtual_ware_house_class
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_cache_storage is not None:
            result['VirtualWareHouseCacheStorage'] = self.virtual_ware_house_cache_storage
        if self.virtual_ware_house_class is not None:
            result['VirtualWareHouseClass'] = self.virtual_ware_house_class
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseCacheStorage') is not None:
            self.virtual_ware_house_cache_storage = m.get('VirtualWareHouseCacheStorage')
        if m.get('VirtualWareHouseClass') is not None:
            self.virtual_ware_house_class = m.get('VirtualWareHouseClass')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class ModifyVirtualWareHouseResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyVirtualWareHouseResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyVirtualWareHouseResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ModifyVirtualWareHouseResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyVirtualWareHouseResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyVirtualWareHouseResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVirtualWareHouseResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PatchClusterSecurityIPGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
        security_ips: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.group_name = group_name
        self.region_id = region_id
        # This parameter is required.
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class PatchClusterSecurityIPGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PatchClusterSecurityIPGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PatchClusterSecurityIPGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PatchClusterSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseVirtualWareHousePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class ReleaseVirtualWareHousePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseVirtualWareHousePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseVirtualWareHousePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseVirtualWareHousePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        dbcluster_id: str = None,
        password: str = None,
        password_sha_256hex: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.password = password
        self.password_sha_256hex = password_sha_256hex
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.password is not None:
            result['Password'] = self.password
        if self.password_sha_256hex is not None:
            result['PasswordSha256Hex'] = self.password_sha_256hex
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PasswordSha256Hex') is not None:
            self.password_sha_256hex = m.get('PasswordSha256Hex')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAccountPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartVirtualWareHouseRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        virtual_ware_house_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id
        # This parameter is required.
        self.virtual_ware_house_id = virtual_ware_house_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.virtual_ware_house_id is not None:
            result['VirtualWareHouseId'] = self.virtual_ware_house_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VirtualWareHouseId') is not None:
            self.virtual_ware_house_id = m.get('VirtualWareHouseId')
        return self


class RestartVirtualWareHouseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartVirtualWareHouseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartVirtualWareHouseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartVirtualWareHouseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpgradeClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpgradeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpsertClusterSecurityIPGroupRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
        security_ips: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.group_name = group_name
        self.region_id = region_id
        # This parameter is required.
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class UpsertClusterSecurityIPGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpsertClusterSecurityIPGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpsertClusterSecurityIPGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpsertClusterSecurityIPGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


