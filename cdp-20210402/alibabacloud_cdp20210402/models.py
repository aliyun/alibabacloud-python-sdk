# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CancelOrderRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CancelOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOrderResponseBody = None,
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
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
    ):
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class CheckClusterNameResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckClusterNameResponseBody = None,
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
            temp_model = CheckClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmNoticeRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class ConfirmNoticeResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmNoticeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmNoticeResponseBody = None,
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
            temp_model = ConfirmNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_info: str = None,
    ):
        self.client_token = client_token
        self.cluster_info = cluster_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class GetClusterDetailRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        instance_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetClusterDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        begin_time: int = None,
        cluster_biz_id: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_status_value: int = None,
        cluster_type: str = None,
        control_center_url: str = None,
        deploy_mode: str = None,
        duration: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_conf: Dict[str, Any] = None,
        notice_confirmed: bool = None,
        order_biz_id: str = None,
        package_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        running_time: int = None,
        version: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.begin_time = begin_time
        self.cluster_biz_id = cluster_biz_id
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_status = cluster_status
        self.cluster_status_value = cluster_status_value
        self.cluster_type = cluster_type
        self.control_center_url = control_center_url
        self.deploy_mode = deploy_mode
        self.duration = duration
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_conf = instance_conf
        self.notice_confirmed = notice_confirmed
        self.order_biz_id = order_biz_id
        self.package_type = package_type
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.running_time = running_time
        self.version = version
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
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_conf is not None:
            result['InstanceConf'] = self.instance_conf
        if self.notice_confirmed is not None:
            result['NoticeConfirmed'] = self.notice_confirmed
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceConf') is not None:
            self.instance_conf = m.get('InstanceConf')
        if m.get('NoticeConfirmed') is not None:
            self.notice_confirmed = m.get('NoticeConfirmed')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetClusterDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetClusterDetailResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetClusterDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterDetailResponseBody = None,
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
            temp_model = GetClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HasDefaultRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasDefaultRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HasDefaultRoleResponseBody = None,
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
            temp_model = HasDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeClouderaDataPlatformResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InitializeClouderaDataPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeClouderaDataPlatformResponseBody = None,
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
            temp_model = InitializeClouderaDataPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDefaultComponentsRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        security_mode: str = None,
    ):
        self.cluster_type = cluster_type
        self.security_mode = security_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.security_mode is not None:
            result['SecurityMode'] = self.security_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('SecurityMode') is not None:
            self.security_mode = m.get('SecurityMode')
        return self


class ListDefaultComponentsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDefaultComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDefaultComponentsResponseBody = None,
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
            temp_model = ListDefaultComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeGroupConstraintsRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
    ):
        self.cluster_type = cluster_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        return self


class ListNodeGroupConstraintsResponseBodyData(TeaModel):
    def __init__(
        self,
        host_group_type: str = None,
        recommended_instance_types: List[str] = None,
        available_data_disk_categories: List[str] = None,
        available_instance_types: List[str] = None,
        available_system_disk_categories: List[str] = None,
        default_data_disk_count: int = None,
        default_data_disk_size: int = None,
        default_node_count: int = None,
        default_system_disk_size: int = None,
        max_data_disk_count: int = None,
        max_data_disk_size: int = None,
        max_node_count: int = None,
        max_system_disk_size: int = None,
        min_data_disk_count: int = None,
        min_data_disk_size: int = None,
        min_node_count: int = None,
        min_system_disk_size: int = None,
        node_group_name: str = None,
    ):
        self.host_group_type = host_group_type
        self.recommended_instance_types = recommended_instance_types
        self.available_data_disk_categories = available_data_disk_categories
        self.available_instance_types = available_instance_types
        self.available_system_disk_categories = available_system_disk_categories
        self.default_data_disk_count = default_data_disk_count
        self.default_data_disk_size = default_data_disk_size
        self.default_node_count = default_node_count
        self.default_system_disk_size = default_system_disk_size
        self.max_data_disk_count = max_data_disk_count
        self.max_data_disk_size = max_data_disk_size
        self.max_node_count = max_node_count
        self.max_system_disk_size = max_system_disk_size
        self.min_data_disk_count = min_data_disk_count
        self.min_data_disk_size = min_data_disk_size
        self.min_node_count = min_node_count
        self.min_system_disk_size = min_system_disk_size
        self.node_group_name = node_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.recommended_instance_types is not None:
            result['RecommendedInstanceTypes'] = self.recommended_instance_types
        if self.available_data_disk_categories is not None:
            result['availableDataDiskCategories'] = self.available_data_disk_categories
        if self.available_instance_types is not None:
            result['availableInstanceTypes'] = self.available_instance_types
        if self.available_system_disk_categories is not None:
            result['availableSystemDiskCategories'] = self.available_system_disk_categories
        if self.default_data_disk_count is not None:
            result['defaultDataDiskCount'] = self.default_data_disk_count
        if self.default_data_disk_size is not None:
            result['defaultDataDiskSize'] = self.default_data_disk_size
        if self.default_node_count is not None:
            result['defaultNodeCount'] = self.default_node_count
        if self.default_system_disk_size is not None:
            result['defaultSystemDiskSize'] = self.default_system_disk_size
        if self.max_data_disk_count is not None:
            result['maxDataDiskCount'] = self.max_data_disk_count
        if self.max_data_disk_size is not None:
            result['maxDataDiskSize'] = self.max_data_disk_size
        if self.max_node_count is not None:
            result['maxNodeCount'] = self.max_node_count
        if self.max_system_disk_size is not None:
            result['maxSystemDiskSize'] = self.max_system_disk_size
        if self.min_data_disk_count is not None:
            result['minDataDiskCount'] = self.min_data_disk_count
        if self.min_data_disk_size is not None:
            result['minDataDiskSize'] = self.min_data_disk_size
        if self.min_node_count is not None:
            result['minNodeCount'] = self.min_node_count
        if self.min_system_disk_size is not None:
            result['minSystemDiskSize'] = self.min_system_disk_size
        if self.node_group_name is not None:
            result['nodeGroupName'] = self.node_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('RecommendedInstanceTypes') is not None:
            self.recommended_instance_types = m.get('RecommendedInstanceTypes')
        if m.get('availableDataDiskCategories') is not None:
            self.available_data_disk_categories = m.get('availableDataDiskCategories')
        if m.get('availableInstanceTypes') is not None:
            self.available_instance_types = m.get('availableInstanceTypes')
        if m.get('availableSystemDiskCategories') is not None:
            self.available_system_disk_categories = m.get('availableSystemDiskCategories')
        if m.get('defaultDataDiskCount') is not None:
            self.default_data_disk_count = m.get('defaultDataDiskCount')
        if m.get('defaultDataDiskSize') is not None:
            self.default_data_disk_size = m.get('defaultDataDiskSize')
        if m.get('defaultNodeCount') is not None:
            self.default_node_count = m.get('defaultNodeCount')
        if m.get('defaultSystemDiskSize') is not None:
            self.default_system_disk_size = m.get('defaultSystemDiskSize')
        if m.get('maxDataDiskCount') is not None:
            self.max_data_disk_count = m.get('maxDataDiskCount')
        if m.get('maxDataDiskSize') is not None:
            self.max_data_disk_size = m.get('maxDataDiskSize')
        if m.get('maxNodeCount') is not None:
            self.max_node_count = m.get('maxNodeCount')
        if m.get('maxSystemDiskSize') is not None:
            self.max_system_disk_size = m.get('maxSystemDiskSize')
        if m.get('minDataDiskCount') is not None:
            self.min_data_disk_count = m.get('minDataDiskCount')
        if m.get('minDataDiskSize') is not None:
            self.min_data_disk_size = m.get('minDataDiskSize')
        if m.get('minNodeCount') is not None:
            self.min_node_count = m.get('minNodeCount')
        if m.get('minSystemDiskSize') is not None:
            self.min_system_disk_size = m.get('minSystemDiskSize')
        if m.get('nodeGroupName') is not None:
            self.node_group_name = m.get('nodeGroupName')
        return self


class ListNodeGroupConstraintsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListNodeGroupConstraintsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNodeGroupConstraintsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNodeGroupConstraintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeGroupConstraintsResponseBody = None,
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
            temp_model = ListNodeGroupConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class ListNodesResponseBodyDataEcsNodeDtoList(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        cpu_count: int = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        expire_time: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        index: int = None,
        instance_type: str = None,
        memory_size: int = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_group_type: str = None,
        node_id: str = None,
        node_name: str = None,
        node_resource_type: str = None,
        node_status: str = None,
        private_ip: str = None,
        public_ip: str = None,
        running_time: int = None,
        serial_number: str = None,
        system_disk_capacity: int = None,
        system_disk_count: int = None,
        system_disk_type: str = None,
    ):
        self.begin_time = begin_time
        self.cpu_count = cpu_count
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.index = index
        self.instance_type = instance_type
        self.memory_size = memory_size
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_group_type = node_group_type
        self.node_id = node_id
        self.node_name = node_name
        self.node_resource_type = node_resource_type
        self.node_status = node_status
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.running_time = running_time
        self.serial_number = serial_number
        self.system_disk_capacity = system_disk_capacity
        self.system_disk_count = system_disk_count
        self.system_disk_type = system_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.index is not None:
            result['Index'] = self.index
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_resource_type is not None:
            result['NodeResourceType'] = self.node_resource_type
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        if self.system_disk_count is not None:
            result['SystemDiskCount'] = self.system_disk_count
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeResourceType') is not None:
            self.node_resource_type = m.get('NodeResourceType')
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        if m.get('SystemDiskCount') is not None:
            self.system_disk_count = m.get('SystemDiskCount')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        return self


class ListNodesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        ecs_node_dto_list: List[ListNodesResponseBodyDataEcsNodeDtoList] = None,
        expire_time: int = None,
        instance_conf: Dict[str, Any] = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.create_time = create_time
        self.ecs_node_dto_list = ecs_node_dto_list
        self.expire_time = expire_time
        self.instance_conf = instance_conf
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        if self.ecs_node_dto_list:
            for k in self.ecs_node_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['EcsNodeDtoList'] = []
        if self.ecs_node_dto_list is not None:
            for k in self.ecs_node_dto_list:
                result['EcsNodeDtoList'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_conf is not None:
            result['InstanceConf'] = self.instance_conf
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.ecs_node_dto_list = []
        if m.get('EcsNodeDtoList') is not None:
            for k in m.get('EcsNodeDtoList'):
                temp_model = ListNodesResponseBodyDataEcsNodeDtoList()
                self.ecs_node_dto_list.append(temp_model.from_map(k))
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceConf') is not None:
            self.instance_conf = m.get('InstanceConf')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListNodesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListNodesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesResponseBody = None,
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
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationsRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        parent_operation_node_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.parent_operation_node_id = parent_operation_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.parent_operation_node_id is not None:
            result['ParentOperationNodeId'] = self.parent_operation_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ParentOperationNodeId') is not None:
            self.parent_operation_node_id = m.get('ParentOperationNodeId')
        return self


class ListOperationsResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        has_child_operation_nodes: bool = None,
        has_operation_task: bool = None,
        operation_id: str = None,
        operation_node_id: str = None,
        operation_node_name: int = None,
        start_time: int = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.has_child_operation_nodes = has_child_operation_nodes
        self.has_operation_task = has_operation_task
        self.operation_id = operation_id
        self.operation_node_id = operation_node_id
        self.operation_node_name = operation_node_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.has_child_operation_nodes is not None:
            result['HasChildOperationNodes'] = self.has_child_operation_nodes
        if self.has_operation_task is not None:
            result['HasOperationTask'] = self.has_operation_task
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_node_id is not None:
            result['OperationNodeId'] = self.operation_node_id
        if self.operation_node_name is not None:
            result['OperationNodeName'] = self.operation_node_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HasChildOperationNodes') is not None:
            self.has_child_operation_nodes = m.get('HasChildOperationNodes')
        if m.get('HasOperationTask') is not None:
            self.has_operation_task = m.get('HasOperationTask')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationNodeId') is not None:
            self.operation_node_id = m.get('OperationNodeId')
        if m.get('OperationNodeName') is not None:
            self.operation_node_name = m.get('OperationNodeName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOperationsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListOperationsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOperationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationsResponseBody = None,
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
            temp_model = ListOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        self.description = description
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListRegionsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListZonesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListZonesResponseBody = None,
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class QueryOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        order_id: str = None,
        order_status: str = None,
        order_type: str = None,
    ):
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class QueryOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryOrderResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrderResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderResponseBody = None,
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
            temp_model = QueryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPriceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        node_group_specs: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.node_group_specs = node_group_specs
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_group_specs is not None:
            result['NodeGroupSpecs'] = self.node_group_specs
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeGroupSpecs') is not None:
            self.node_group_specs = m.get('NodeGroupSpecs')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryPriceResponseBodyDataEcsPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryPriceResponseBodyDataSoftPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        ecs_price_info: QueryPriceResponseBodyDataEcsPriceInfo = None,
        soft_price_info: QueryPriceResponseBodyDataSoftPriceInfo = None,
        sum_price: float = None,
    ):
        self.discount_price = discount_price
        self.ecs_price_info = ecs_price_info
        self.soft_price_info = soft_price_info
        self.sum_price = sum_price

    def validate(self):
        if self.ecs_price_info:
            self.ecs_price_info.validate()
        if self.soft_price_info:
            self.soft_price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.ecs_price_info is not None:
            result['EcsPriceInfo'] = self.ecs_price_info.to_map()
        if self.soft_price_info is not None:
            result['SoftPriceInfo'] = self.soft_price_info.to_map()
        if self.sum_price is not None:
            result['SumPrice'] = self.sum_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('EcsPriceInfo') is not None:
            temp_model = QueryPriceResponseBodyDataEcsPriceInfo()
            self.ecs_price_info = temp_model.from_map(m['EcsPriceInfo'])
        if m.get('SoftPriceInfo') is not None:
            temp_model = QueryPriceResponseBodyDataSoftPriceInfo()
            self.soft_price_info = temp_model.from_map(m['SoftPriceInfo'])
        if m.get('SumPrice') is not None:
            self.sum_price = m.get('SumPrice')
        return self


class QueryPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryPriceResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPriceResponseBody = None,
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
            temp_model = QueryPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewOrderRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        return self


class QueryRenewOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRenewOrderResponseBody = None,
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
            temp_model = QueryRenewOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewPriceRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        instances: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instances is not None:
            result['Instances'] = self.instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        return self


class QueryRenewPriceResponseBodyDataCdpSoftPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryRenewPriceResponseBodyDataEcsPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryRenewPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        cdp_soft_price_info: QueryRenewPriceResponseBodyDataCdpSoftPriceInfo = None,
        discount_price: float = None,
        ecs_price_info: QueryRenewPriceResponseBodyDataEcsPriceInfo = None,
        sum_price: float = None,
    ):
        self.cdp_soft_price_info = cdp_soft_price_info
        self.discount_price = discount_price
        self.ecs_price_info = ecs_price_info
        self.sum_price = sum_price

    def validate(self):
        if self.cdp_soft_price_info:
            self.cdp_soft_price_info.validate()
        if self.ecs_price_info:
            self.ecs_price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdp_soft_price_info is not None:
            result['CdpSoftPriceInfo'] = self.cdp_soft_price_info.to_map()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.ecs_price_info is not None:
            result['EcsPriceInfo'] = self.ecs_price_info.to_map()
        if self.sum_price is not None:
            result['SumPrice'] = self.sum_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdpSoftPriceInfo') is not None:
            temp_model = QueryRenewPriceResponseBodyDataCdpSoftPriceInfo()
            self.cdp_soft_price_info = temp_model.from_map(m['CdpSoftPriceInfo'])
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('EcsPriceInfo') is not None:
            temp_model = QueryRenewPriceResponseBodyDataEcsPriceInfo()
            self.ecs_price_info = temp_model.from_map(m['EcsPriceInfo'])
        if m.get('SumPrice') is not None:
            self.sum_price = m.get('SumPrice')
        return self


class QueryRenewPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryRenewPriceResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRenewPriceResponseBody = None,
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
            temp_model = QueryRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScaleUpOrderRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        instance_id: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryScaleUpOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScaleUpOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryScaleUpOrderResponseBody = None,
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
            temp_model = QueryScaleUpOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScaleUpPriceRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        core_number: int = None,
        duration: int = None,
        instance_id: str = None,
        instance_type: str = None,
        node_group_type: str = None,
        pricing_cycle: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.core_number = core_number
        self.duration = duration
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.node_group_type = node_group_type
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.core_number is not None:
            result['CoreNumber'] = self.core_number
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CoreNumber') is not None:
            self.core_number = m.get('CoreNumber')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class QueryScaleUpPriceResponseBodyDataEcsPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryScaleUpPriceResponseBodyDataSoftPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryScaleUpPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        ecs_price_info: QueryScaleUpPriceResponseBodyDataEcsPriceInfo = None,
        soft_price_info: QueryScaleUpPriceResponseBodyDataSoftPriceInfo = None,
        sum_price: float = None,
    ):
        self.discount_price = discount_price
        self.ecs_price_info = ecs_price_info
        self.soft_price_info = soft_price_info
        self.sum_price = sum_price

    def validate(self):
        if self.ecs_price_info:
            self.ecs_price_info.validate()
        if self.soft_price_info:
            self.soft_price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.ecs_price_info is not None:
            result['EcsPriceInfo'] = self.ecs_price_info.to_map()
        if self.soft_price_info is not None:
            result['SoftPriceInfo'] = self.soft_price_info.to_map()
        if self.sum_price is not None:
            result['SumPrice'] = self.sum_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('EcsPriceInfo') is not None:
            temp_model = QueryScaleUpPriceResponseBodyDataEcsPriceInfo()
            self.ecs_price_info = temp_model.from_map(m['EcsPriceInfo'])
        if m.get('SoftPriceInfo') is not None:
            temp_model = QueryScaleUpPriceResponseBodyDataSoftPriceInfo()
            self.soft_price_info = temp_model.from_map(m['SoftPriceInfo'])
        if m.get('SumPrice') is not None:
            self.sum_price = m.get('SumPrice')
        return self


class QueryScaleUpPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryScaleUpPriceResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryScaleUpPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScaleUpPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryScaleUpPriceResponseBody = None,
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
            temp_model = QueryScaleUpPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReleaseClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseClusterResponseBody = None,
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
            temp_model = ReleaseClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        instances: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.instances is not None:
            result['Instances'] = self.instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: RenewInstanceResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewInstanceResponseBody = None,
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleUpClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        core_number: int = None,
        duration: int = None,
        instance_id: str = None,
        instance_type: str = None,
        node_group_type: str = None,
        pricing_cycle: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.core_number = core_number
        self.duration = duration
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.node_group_type = node_group_type
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.core_number is not None:
            result['CoreNumber'] = self.core_number
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CoreNumber') is not None:
            self.core_number = m.get('CoreNumber')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class ScaleUpClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleUpClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleUpClusterResponseBody = None,
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
            temp_model = ScaleUpClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchClusterInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchClusterInstancesResponseBodyDataClusterInstanceInfo(TeaModel):
    def __init__(
        self,
        control_center_login_name: str = None,
        control_center_url: str = None,
        sg_id: str = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        self.control_center_login_name = control_center_login_name
        self.control_center_url = control_center_url
        self.sg_id = sg_id
        self.vpc_id = vpc_id
        self.vsw_id = vsw_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_center_login_name is not None:
            result['ControlCenterLoginName'] = self.control_center_login_name
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlCenterLoginName') is not None:
            self.control_center_login_name = m.get('ControlCenterLoginName')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')
        return self


class SearchClusterInstancesResponseBodyDataEcsGroupList(TeaModel):
    def __init__(
        self,
        cpu_count: int = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        host_group_name: str = None,
        host_group_type: str = None,
        instance_type: str = None,
        memory_size: int = None,
        node_count: int = None,
        system_disk_capacity: str = None,
        system_disk_count: int = None,
        system_disk_type: str = None,
    ):
        self.cpu_count = cpu_count
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.host_group_name = host_group_name
        self.host_group_type = host_group_type
        self.instance_type = instance_type
        self.memory_size = memory_size
        self.node_count = node_count
        self.system_disk_capacity = system_disk_capacity
        self.system_disk_count = system_disk_count
        self.system_disk_type = system_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        if self.system_disk_count is not None:
            result['SystemDiskCount'] = self.system_disk_count
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        if m.get('SystemDiskCount') is not None:
            self.system_disk_count = m.get('SystemDiskCount')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        return self


class SearchClusterInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        cluster_biz_id: str = None,
        cluster_id: str = None,
        cluster_instance_info: SearchClusterInstancesResponseBodyDataClusterInstanceInfo = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_status_value: int = None,
        cluster_type: str = None,
        control_center_url: str = None,
        duration: int = None,
        ecs_group_list: List[SearchClusterInstancesResponseBodyDataEcsGroupList] = None,
        expire_time: int = None,
        fail_reason: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_conf: Dict[str, Any] = None,
        notice_confirmed: bool = None,
        order_biz_id: str = None,
        package_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        running_time: int = None,
        zone_id: str = None,
    ):
        self.begin_time = begin_time
        self.cluster_biz_id = cluster_biz_id
        self.cluster_id = cluster_id
        self.cluster_instance_info = cluster_instance_info
        self.cluster_name = cluster_name
        self.cluster_status = cluster_status
        self.cluster_status_value = cluster_status_value
        self.cluster_type = cluster_type
        self.control_center_url = control_center_url
        self.duration = duration
        self.ecs_group_list = ecs_group_list
        self.expire_time = expire_time
        self.fail_reason = fail_reason
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_conf = instance_conf
        self.notice_confirmed = notice_confirmed
        self.order_biz_id = order_biz_id
        self.package_type = package_type
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.running_time = running_time
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_instance_info:
            self.cluster_instance_info.validate()
        if self.ecs_group_list:
            for k in self.ecs_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_instance_info is not None:
            result['ClusterInstanceInfo'] = self.cluster_instance_info.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.duration is not None:
            result['Duration'] = self.duration
        result['EcsGroupList'] = []
        if self.ecs_group_list is not None:
            for k in self.ecs_group_list:
                result['EcsGroupList'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_conf is not None:
            result['InstanceConf'] = self.instance_conf
        if self.notice_confirmed is not None:
            result['NoticeConfirmed'] = self.notice_confirmed
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInstanceInfo') is not None:
            temp_model = SearchClusterInstancesResponseBodyDataClusterInstanceInfo()
            self.cluster_instance_info = temp_model.from_map(m['ClusterInstanceInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.ecs_group_list = []
        if m.get('EcsGroupList') is not None:
            for k in m.get('EcsGroupList'):
                temp_model = SearchClusterInstancesResponseBodyDataEcsGroupList()
                self.ecs_group_list.append(temp_model.from_map(k))
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceConf') is not None:
            self.instance_conf = m.get('InstanceConf')
        if m.get('NoticeConfirmed') is not None:
            self.notice_confirmed = m.get('NoticeConfirmed')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchClusterInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SearchClusterInstancesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchClusterInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchClusterInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchClusterInstancesResponseBody = None,
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
            temp_model = SearchClusterInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleOrderRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SingleOrderResponseBodyDataEcsGroupList(TeaModel):
    def __init__(
        self,
        cpu_count: int = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        host_group_name: str = None,
        host_group_type: str = None,
        instance_type: str = None,
        memory_size: int = None,
        node_count: int = None,
        system_disk_capacity: int = None,
        system_disk_count: int = None,
        system_disk_type: str = None,
    ):
        self.cpu_count = cpu_count
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.host_group_name = host_group_name
        self.host_group_type = host_group_type
        self.instance_type = instance_type
        self.memory_size = memory_size
        self.node_count = node_count
        self.system_disk_capacity = system_disk_capacity
        self.system_disk_count = system_disk_count
        self.system_disk_type = system_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.system_disk_capacity is not None:
            result['SystemDiskCapacity'] = self.system_disk_capacity
        if self.system_disk_count is not None:
            result['SystemDiskCount'] = self.system_disk_count
        if self.system_disk_type is not None:
            result['SystemDiskType'] = self.system_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('SystemDiskCapacity') is not None:
            self.system_disk_capacity = m.get('SystemDiskCapacity')
        if m.get('SystemDiskCount') is not None:
            self.system_disk_count = m.get('SystemDiskCount')
        if m.get('SystemDiskType') is not None:
            self.system_disk_type = m.get('SystemDiskType')
        return self


class SingleOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_size: int = None,
        cluster_status: int = None,
        deploy_mode: str = None,
        duration: int = None,
        ecs_group_list: List[SingleOrderResponseBodyDataEcsGroupList] = None,
        instance_id: str = None,
        order_id: str = None,
        package_type: str = None,
        pricing_cycle: str = None,
        storage_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_size = cluster_size
        self.cluster_status = cluster_status
        self.deploy_mode = deploy_mode
        self.duration = duration
        self.ecs_group_list = ecs_group_list
        self.instance_id = instance_id
        self.order_id = order_id
        self.package_type = package_type
        self.pricing_cycle = pricing_cycle
        self.storage_size = storage_size

    def validate(self):
        if self.ecs_group_list:
            for k in self.ecs_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_size is not None:
            result['ClusterSize'] = self.cluster_size
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.duration is not None:
            result['Duration'] = self.duration
        result['EcsGroupList'] = []
        if self.ecs_group_list is not None:
            for k in self.ecs_group_list:
                result['EcsGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSize') is not None:
            self.cluster_size = m.get('ClusterSize')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.ecs_group_list = []
        if m.get('EcsGroupList') is not None:
            for k in m.get('EcsGroupList'):
                temp_model = SingleOrderResponseBodyDataEcsGroupList()
                self.ecs_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class SingleOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: SingleOrderResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SingleOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SingleOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SingleOrderResponseBody = None,
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
            temp_model = SingleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        cluster_name: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class UpdateClusterNameResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateClusterNameResponseBody = None,
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
            temp_model = UpdateClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadLicenseResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class UploadLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadLicenseResponseBody = None,
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
            temp_model = UploadLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


