# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DataImageRegionDistributeMapValue(TeaModel):
    def __init__(
        self,
        distribute_status: str = None,
        progress: str = None,
    ):
        self.distribute_status = distribute_status
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribute_status is not None:
            result['DistributeStatus'] = self.distribute_status
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeStatus') is not None:
            self.distribute_status = m.get('DistributeStatus')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class AttachKeyPairRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        key_pair_id: str = None,
    ):
        self.instance_ids = instance_ids
        # This parameter is required.
        self.key_pair_id = key_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        return self


class AttachKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        attached_instance_ids: List[str] = None,
        fail_count: int = None,
        key_pair_id: str = None,
        total_count: int = None,
    ):
        self.attached_instance_ids = attached_instance_ids
        self.fail_count = fail_count
        self.key_pair_id = key_pair_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_instance_ids is not None:
            result['AttachedInstanceIds'] = self.attached_instance_ids
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedInstanceIds') is not None:
            self.attached_instance_ids = m.get('AttachedInstanceIds')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AttachKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: AttachKeyPairResponseBodyData = None,
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
            temp_model = AttachKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachKeyPairResponseBody = None,
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
            temp_model = AttachKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        authorize_user_id: str = None,
        un_authorize_user_id: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.authorize_user_id = authorize_user_id
        self.un_authorize_user_id = un_authorize_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.authorize_user_id is not None:
            result['AuthorizeUserId'] = self.authorize_user_id
        if self.un_authorize_user_id is not None:
            result['UnAuthorizeUserId'] = self.un_authorize_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('AuthorizeUserId') is not None:
            self.authorize_user_id = m.get('AuthorizeUserId')
        if m.get('UnAuthorizeUserId') is not None:
            self.un_authorize_user_id = m.get('UnAuthorizeUserId')
        return self


class AuthorizeAndroidInstanceResponseBody(TeaModel):
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


class AuthorizeAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeAndroidInstanceResponseBody = None,
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
            temp_model = AuthorizeAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BackupFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_file_path: str = None,
        description: str = None,
        source_app_list: List[str] = None,
        source_file_path_list: List[str] = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # This parameter is required.
        self.backup_file_path = backup_file_path
        self.description = description
        self.source_app_list = source_app_list
        self.source_file_path_list = source_file_path_list
        self.upload_endpoint = upload_endpoint
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path
        if self.description is not None:
            result['Description'] = self.description
        if self.source_app_list is not None:
            result['SourceAppList'] = self.source_app_list
        if self.source_file_path_list is not None:
            result['SourceFilePathList'] = self.source_file_path_list
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceAppList') is not None:
            self.source_app_list = m.get('SourceAppList')
        if m.get('SourceFilePathList') is not None:
            self.source_file_path_list = m.get('SourceFilePathList')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class BackupFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.backup_file_id = backup_file_id
        self.backup_file_name = backup_file_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BackupFileResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data: List[BackupFileResponseBodyData] = None,
        request_id: str = None,
    ):
        self.count = count
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
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BackupFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BackupFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BackupFileResponseBody = None,
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
            temp_model = BackupFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResourceStockRequest(TeaModel):
    def __init__(
        self,
        acp_spec_id: str = None,
        amount: int = None,
        biz_region_id: str = None,
        gpu_acceleration: bool = None,
        zone_id: str = None,
    ):
        self.acp_spec_id = acp_spec_id
        self.amount = amount
        # This parameter is required.
        self.biz_region_id = biz_region_id
        self.gpu_acceleration = gpu_acceleration
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acp_spec_id is not None:
            result['AcpSpecId'] = self.acp_spec_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcpSpecId') is not None:
            self.acp_spec_id = m.get('AcpSpecId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckResourceStockResponseBodyResourceStockModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stock_status: str = None,
        zone_id: str = None,
    ):
        self.region_id = region_id
        self.stock_status = stock_status
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
        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckResourceStockResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_stock_models: List[CheckResourceStockResponseBodyResourceStockModels] = None,
    ):
        self.request_id = request_id
        self.resource_stock_models = resource_stock_models

    def validate(self):
        if self.resource_stock_models:
            for k in self.resource_stock_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceStockModels'] = []
        if self.resource_stock_models is not None:
            for k in self.resource_stock_models:
                result['ResourceStockModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_stock_models = []
        if m.get('ResourceStockModels') is not None:
            for k in m.get('ResourceStockModels'):
                temp_model = CheckResourceStockResponseBodyResourceStockModels()
                self.resource_stock_models.append(temp_model.from_map(k))
        return self


class CheckResourceStockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckResourceStockResponseBody = None,
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
            temp_model = CheckResourceStockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_type: str = None,
        client_token: str = None,
        gpu_acceleration: bool = None,
        image_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        key_pair_id: str = None,
        number_of_instances: int = None,
        office_site_id: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        v_switch_id: str = None,
    ):
        self.amount = amount
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        # This parameter is required.
        self.biz_region_id = biz_region_id
        self.charge_type = charge_type
        self.client_token = client_token
        self.gpu_acceleration = gpu_acceleration
        # This parameter is required.
        self.image_id = image_id
        self.instance_group_name = instance_group_name
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
        self.key_pair_id = key_pair_id
        self.number_of_instances = number_of_instances
        self.office_site_id = office_site_id
        self.period = period
        self.period_unit = period_unit
        # This parameter is required.
        self.policy_group_id = policy_group_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos(TeaModel):
    def __init__(
        self,
        instance_group_id: str = None,
        instance_ids: List[str] = None,
    ):
        self.instance_group_id = instance_group_id
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class CreateAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
        instance_group_infos: List[CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.instance_group_ids = instance_group_ids
        self.instance_group_infos = instance_group_infos
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.instance_group_infos:
            for k in self.instance_group_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        result['InstanceGroupInfos'] = []
        if self.instance_group_infos is not None:
            for k in self.instance_group_infos:
                result['InstanceGroupInfos'].append(k.to_map() if k else None)
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        self.instance_group_infos = []
        if m.get('InstanceGroupInfos') is not None:
            for k in m.get('InstanceGroupInfos'):
                temp_model = CreateAndroidInstanceGroupResponseBodyInstanceGroupInfos()
                self.instance_group_infos.append(temp_model.from_map(k))
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAndroidInstanceGroupResponseBody = None,
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
            temp_model = CreateAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        biz_region_id: str = None,
        description: str = None,
        file_name: str = None,
        file_path: str = None,
        icon_url: str = None,
        install_param: str = None,
        oss_app_url: str = None,
    ):
        self.app_name = app_name
        self.biz_region_id = biz_region_id
        self.description = description
        self.file_name = file_name
        self.file_path = file_path
        self.icon_url = icon_url
        self.install_param = install_param
        self.oss_app_url = oss_app_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.install_param is not None:
            result['InstallParam'] = self.install_param
        if self.oss_app_url is not None:
            result['OssAppUrl'] = self.oss_app_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('InstallParam') is not None:
            self.install_param = m.get('InstallParam')
        if m.get('OssAppUrl') is not None:
            self.oss_app_url = m.get('OssAppUrl')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        image_name: str = None,
        instance_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.image_name = image_name
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateCustomImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomImageResponseBody = None,
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
            temp_model = CreateCustomImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
    ):
        # This parameter is required.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class CreateKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
        private_key_body: str = None,
    ):
        self.gmt_created = gmt_created
        self.key_pair_id = key_pair_id
        self.key_pair_name = key_pair_name
        self.private_key_body = private_key_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.private_key_body is not None:
            result['PrivateKeyBody'] = self.private_key_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PrivateKeyBody') is not None:
            self.private_key_body = m.get('PrivateKeyBody')
        return self


class CreateKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateKeyPairResponseBodyData = None,
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
            temp_model = CreateKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKeyPairResponseBody = None,
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
            temp_model = CreateKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyGroupRequestNetRedirectPolicy(TeaModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
    ):
        self.custom_proxy = custom_proxy
        self.host_addr = host_addr
        self.net_redirect = net_redirect
        self.port = port
        self.proxy_password = proxy_password
        self.proxy_type = proxy_type
        self.proxy_user_name = proxy_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy
        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')
        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: CreatePolicyGroupRequestNetRedirectPolicy = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.camera_redirect = camera_redirect
        self.clipboard = clipboard
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.lock_resolution = lock_resolution
        self.net_redirect_policy = net_redirect_policy
        self.policy_group_name = policy_group_name
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            temp_model = CreatePolicyGroupRequestNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m['NetRedirectPolicy'])
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class CreatePolicyGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy_shrink: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.camera_redirect = camera_redirect
        self.clipboard = clipboard
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.lock_resolution = lock_resolution
        self.net_redirect_policy_shrink = net_redirect_policy_shrink
        self.policy_group_name = policy_group_name
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy_shrink is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy_shrink
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            self.net_redirect_policy_shrink = m.get('NetRedirectPolicy')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class CreatePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        request_id: str = None,
    ):
        self.policy_group_id = policy_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyGroupResponseBody = None,
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
            temp_model = CreatePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        instance_group_ids: List[str] = None,
    ):
        self.instance_group_ids = instance_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        return self


class DeleteAndroidInstanceGroupResponseBody(TeaModel):
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


class DeleteAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAndroidInstanceGroupResponseBody = None,
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
            temp_model = DeleteAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppsRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
    ):
        self.app_id_list = app_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        return self


class DeleteAppsResponseBody(TeaModel):
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


class DeleteAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppsResponseBody = None,
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
            temp_model = DeleteAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(
        self,
        image_ids: List[str] = None,
    ):
        # This parameter is required.
        self.image_ids = image_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        return self


class DeleteImagesShrinkRequest(TeaModel):
    def __init__(
        self,
        image_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.image_ids_shrink = image_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids_shrink is not None:
            result['ImageIds'] = self.image_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids_shrink = m.get('ImageIds')
        return self


class DeleteImagesResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_delete_image_ids: List[str] = None,
        success_delete_image_ids: List[str] = None,
    ):
        self.fail_delete_image_ids = fail_delete_image_ids
        self.success_delete_image_ids = success_delete_image_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_delete_image_ids is not None:
            result['FailDeleteImageIds'] = self.fail_delete_image_ids
        if self.success_delete_image_ids is not None:
            result['SuccessDeleteImageIds'] = self.success_delete_image_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailDeleteImageIds') is not None:
            self.fail_delete_image_ids = m.get('FailDeleteImageIds')
        if m.get('SuccessDeleteImageIds') is not None:
            self.success_delete_image_ids = m.get('SuccessDeleteImageIds')
        return self


class DeleteImagesResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteImagesResponseBodyData = None,
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
            temp_model = DeleteImagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImagesResponseBody = None,
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
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_ids: List[str] = None,
    ):
        self.key_pair_ids = key_pair_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_ids is not None:
            result['KeyPairIds'] = self.key_pair_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairIds') is not None:
            self.key_pair_ids = m.get('KeyPairIds')
        return self


class DeleteKeyPairsResponseBody(TeaModel):
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


class DeleteKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeyPairsResponseBody = None,
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
            temp_model = DeleteKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        policy_group_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_group_ids = policy_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')
        return self


class DeletePolicyGroupResponseBody(TeaModel):
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


class DeletePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyGroupResponseBody = None,
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
            temp_model = DeletePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAndroidInstanceGroupsRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        charge_type: str = None,
        instance_group_ids: List[str] = None,
        instance_group_name: str = None,
        key_pair_id: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_group_id: str = None,
        sale_mode: str = None,
        status: str = None,
    ):
        self.biz_region_id = biz_region_id
        self.charge_type = charge_type
        self.instance_group_ids = instance_group_ids
        self.instance_group_name = instance_group_name
        self.key_pair_id = key_pair_id
        self.max_results = max_results
        self.next_token = next_token
        self.policy_group_id = policy_group_id
        self.sale_mode = sale_mode
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        self.disk_size = disk_size
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel(TeaModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        architecture_type: str = None,
        charge_type: str = None,
        cpu: str = None,
        disks: List[DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks] = None,
        error_code: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        installed_app_list: str = None,
        instance_group_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        instance_group_spec_describe: str = None,
        instance_group_status: str = None,
        memory: int = None,
        number_of_instances: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        rendering_type: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        sale_mode: str = None,
        system_version: str = None,
        v_switch_id: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.architecture_type = architecture_type
        self.charge_type = charge_type
        self.cpu = cpu
        self.disks = disks
        self.error_code = error_code
        self.gmt_create = gmt_create
        self.gmt_expired = gmt_expired
        self.gmt_modified = gmt_modified
        self.image_id = image_id
        self.installed_app_list = installed_app_list
        self.instance_group_id = instance_group_id
        self.instance_group_name = instance_group_name
        self.instance_group_spec = instance_group_spec
        self.instance_group_spec_describe = instance_group_spec_describe
        self.instance_group_status = instance_group_status
        self.memory = memory
        self.number_of_instances = number_of_instances
        self.office_site_id = office_site_id
        self.policy_group_id = policy_group_id
        self.region_id = region_id
        self.rendering_type = rendering_type
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width
        self.sale_mode = sale_mode
        self.system_version = system_version
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.installed_app_list is not None:
            result['InstalledAppList'] = self.installed_app_list
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec
        if self.instance_group_spec_describe is not None:
            result['InstanceGroupSpecDescribe'] = self.instance_group_spec_describe
        if self.instance_group_status is not None:
            result['InstanceGroupStatus'] = self.instance_group_status
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.system_version is not None:
            result['SystemVersion'] = self.system_version
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModelDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstalledAppList') is not None:
            self.installed_app_list = m.get('InstalledAppList')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')
        if m.get('InstanceGroupSpecDescribe') is not None:
            self.instance_group_spec_describe = m.get('InstanceGroupSpecDescribe')
        if m.get('InstanceGroupStatus') is not None:
            self.instance_group_status = m.get('InstanceGroupStatus')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('SystemVersion') is not None:
            self.system_version = m.get('SystemVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeAndroidInstanceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        instance_group_model: List[DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instance_group_model = instance_group_model
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instance_group_model:
            for k in self.instance_group_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceGroupModel'] = []
        if self.instance_group_model is not None:
            for k in self.instance_group_model:
                result['InstanceGroupModel'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_group_model = []
        if m.get('InstanceGroupModel') is not None:
            for k in m.get('InstanceGroupModel'):
                temp_model = DescribeAndroidInstanceGroupsResponseBodyInstanceGroupModel()
                self.instance_group_model.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAndroidInstanceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAndroidInstanceGroupsResponseBody = None,
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
            temp_model = DescribeAndroidInstanceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAndroidInstancesRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        android_instance_name: str = None,
        charge_type: str = None,
        instance_group_id: str = None,
        instance_group_ids: List[str] = None,
        instance_group_name: str = None,
        key_pair_id: str = None,
        max_results: int = None,
        next_token: str = None,
        sale_mode: str = None,
        status: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.android_instance_name = android_instance_name
        self.charge_type = charge_type
        self.instance_group_id = instance_group_id
        self.instance_group_ids = instance_group_ids
        self.instance_group_name = instance_group_name
        self.key_pair_id = key_pair_id
        self.max_results = max_results
        self.next_token = next_token
        self.sale_mode = sale_mode
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAndroidInstancesResponseBodyInstanceModelDisks(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        self.disk_size = disk_size
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeAndroidInstancesResponseBodyInstanceModel(TeaModel):
    def __init__(
        self,
        android_instance_group_id: str = None,
        android_instance_group_name: str = None,
        android_instance_id: str = None,
        android_instance_name: str = None,
        android_instance_status: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        authorized_user_id: str = None,
        bind_user_id: str = None,
        charge_type: str = None,
        cpu: str = None,
        disks: List[DescribeAndroidInstancesResponseBodyInstanceModelDisks] = None,
        error_code: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        instance_type: str = None,
        key_pair_id: str = None,
        memory: int = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        persistent_app_instance_id: str = None,
        policy_group_id: str = None,
        rate: int = None,
        region_id: str = None,
        rendering_type: str = None,
    ):
        self.android_instance_group_id = android_instance_group_id
        self.android_instance_group_name = android_instance_group_name
        self.android_instance_id = android_instance_id
        self.android_instance_name = android_instance_name
        self.android_instance_status = android_instance_status
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.authorized_user_id = authorized_user_id
        self.bind_user_id = bind_user_id
        self.charge_type = charge_type
        self.cpu = cpu
        self.disks = disks
        self.error_code = error_code
        self.gmt_create = gmt_create
        self.gmt_expired = gmt_expired
        self.gmt_modified = gmt_modified
        self.instance_type = instance_type
        self.key_pair_id = key_pair_id
        self.memory = memory
        self.network_interface_ip = network_interface_ip
        self.office_site_id = office_site_id
        self.persistent_app_instance_id = persistent_app_instance_id
        self.policy_group_id = policy_group_id
        self.rate = rate
        self.region_id = region_id
        self.rendering_type = rendering_type

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_group_id is not None:
            result['AndroidInstanceGroupId'] = self.android_instance_group_id
        if self.android_instance_group_name is not None:
            result['AndroidInstanceGroupName'] = self.android_instance_group_name
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.android_instance_status is not None:
            result['AndroidInstanceStatus'] = self.android_instance_status
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        if self.bind_user_id is not None:
            result['BindUserId'] = self.bind_user_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.persistent_app_instance_id is not None:
            result['PersistentAppInstanceId'] = self.persistent_app_instance_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceGroupId') is not None:
            self.android_instance_group_id = m.get('AndroidInstanceGroupId')
        if m.get('AndroidInstanceGroupName') is not None:
            self.android_instance_group_name = m.get('AndroidInstanceGroupName')
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('AndroidInstanceStatus') is not None:
            self.android_instance_status = m.get('AndroidInstanceStatus')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        if m.get('BindUserId') is not None:
            self.bind_user_id = m.get('BindUserId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeAndroidInstancesResponseBodyInstanceModelDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PersistentAppInstanceId') is not None:
            self.persistent_app_instance_id = m.get('PersistentAppInstanceId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')
        return self


class DescribeAndroidInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_model: List[DescribeAndroidInstancesResponseBodyInstanceModel] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instance_model = instance_model
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instance_model:
            for k in self.instance_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceModel'] = []
        if self.instance_model is not None:
            for k in self.instance_model:
                result['InstanceModel'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_model = []
        if m.get('InstanceModel') is not None:
            for k in m.get('InstanceModel'):
                temp_model = DescribeAndroidInstancesResponseBodyInstanceModel()
                self.instance_model.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAndroidInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAndroidInstancesResponseBody = None,
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
            temp_model = DescribeAndroidInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        app_name: str = None,
        biz_region_id: str = None,
        installation_status: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        self.app_id_list = app_id_list
        self.app_name = app_name
        self.biz_region_id = biz_region_id
        self.installation_status = installation_status
        self.max_results = max_results
        self.next_token = next_token
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.installation_status is not None:
            result['InstallationStatus'] = self.installation_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('InstallationStatus') is not None:
            self.installation_status = m.get('InstallationStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        android_app_version: str = None,
        app_id: int = None,
        app_name: str = None,
        biz_region_id: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_url: str = None,
        installation_status: str = None,
        instance_group_list: List[str] = None,
        package_name: str = None,
        status: str = None,
    ):
        self.android_app_version = android_app_version
        self.app_id = app_id
        self.app_name = app_name
        self.biz_region_id = biz_region_id
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icon_url = icon_url
        self.installation_status = installation_status
        self.instance_group_list = instance_group_list
        self.package_name = package_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_app_version is not None:
            result['AndroidAppVersion'] = self.android_app_version
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.installation_status is not None:
            result['InstallationStatus'] = self.installation_status
        if self.instance_group_list is not None:
            result['InstanceGroupList'] = self.instance_group_list
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidAppVersion') is not None:
            self.android_app_version = m.get('AndroidAppVersion')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('InstallationStatus') is not None:
            self.installation_status = m.get('InstallationStatus')
        if m.get('InstanceGroupList') is not None:
            self.instance_group_list = m.get('InstanceGroupList')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeAppsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.data = data
        self.next_token = next_token
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
                temp_model = DescribeAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppsResponseBody = None,
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
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupFilesRequest(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        android_instance_name: str = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        description: str = None,
        end_time: str = None,
        end_user_id: str = None,
        instance_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        start_time: str = None,
        status_list: List[str] = None,
    ):
        self.android_instance_id = android_instance_id
        self.android_instance_name = android_instance_name
        self.backup_file_id = backup_file_id
        self.backup_file_name = backup_file_name
        self.description = description
        self.end_time = end_time
        self.end_user_id = end_user_id
        self.instance_group_id = instance_group_id
        self.max_results = max_results
        self.next_token = next_token
        self.start_time = start_time
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class DescribeBackupFilesResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        android_instance_name: str = None,
        backup_file_id: str = None,
        backup_file_name: str = None,
        backup_file_path: str = None,
        description: str = None,
        end_user_id: str = None,
        file_size: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_group_id: str = None,
        region_id: str = None,
        source_app_info_list: List[str] = None,
        source_file_path_list: List[str] = None,
        status: str = None,
        task_id: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.android_instance_name = android_instance_name
        self.backup_file_id = backup_file_id
        self.backup_file_name = backup_file_name
        self.backup_file_path = backup_file_path
        self.description = description
        self.end_user_id = end_user_id
        self.file_size = file_size
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.instance_group_id = instance_group_id
        self.region_id = region_id
        self.source_app_info_list = source_app_info_list
        self.source_file_path_list = source_file_path_list
        self.status = status
        self.task_id = task_id
        self.upload_endpoint = upload_endpoint
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.android_instance_name is not None:
            result['AndroidInstanceName'] = self.android_instance_name
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_name is not None:
            result['BackupFileName'] = self.backup_file_name
        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path
        if self.description is not None:
            result['Description'] = self.description
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_app_info_list is not None:
            result['SourceAppInfoList'] = self.source_app_info_list
        if self.source_file_path_list is not None:
            result['SourceFilePathList'] = self.source_file_path_list
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('AndroidInstanceName') is not None:
            self.android_instance_name = m.get('AndroidInstanceName')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFileName') is not None:
            self.backup_file_name = m.get('BackupFileName')
        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceAppInfoList') is not None:
            self.source_app_info_list = m.get('SourceAppInfoList')
        if m.get('SourceFilePathList') is not None:
            self.source_file_path_list = m.get('SourceFilePathList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class DescribeBackupFilesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeBackupFilesResponseBodyData] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeBackupFilesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBackupFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupFilesResponseBody = None,
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
            temp_model = DescribeBackupFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageListRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        # This parameter is required.
        self.image_type = image_type
        self.max_results = max_results
        self.next_token = next_token
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeImageListResponseBodyData(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        image_name: str = None,
        image_region_distribute_map: Dict[str, DataImageRegionDistributeMapValue] = None,
        image_region_list: List[str] = None,
        image_type: str = None,
        language: str = None,
        release_time: str = None,
        rendering_type: str = None,
        status: str = None,
        system_type: str = None,
    ):
        self.ali_uid = ali_uid
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.image_id = image_id
        self.image_name = image_name
        self.image_region_distribute_map = image_region_distribute_map
        self.image_region_list = image_region_list
        self.image_type = image_type
        self.language = language
        self.release_time = release_time
        self.rendering_type = rendering_type
        self.status = status
        self.system_type = system_type

    def validate(self):
        if self.image_region_distribute_map:
            for v in self.image_region_distribute_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        result['ImageRegionDistributeMap'] = {}
        if self.image_region_distribute_map is not None:
            for k, v in self.image_region_distribute_map.items():
                result['ImageRegionDistributeMap'][k] = v.to_map()
        if self.image_region_list is not None:
            result['ImageRegionList'] = self.image_region_list
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.language is not None:
            result['Language'] = self.language
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type
        if self.status is not None:
            result['Status'] = self.status
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        self.image_region_distribute_map = {}
        if m.get('ImageRegionDistributeMap') is not None:
            for k, v in m.get('ImageRegionDistributeMap').items():
                temp_model = DataImageRegionDistributeMapValue()
                self.image_region_distribute_map[k] = temp_model.from_map(v)
        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        return self


class DescribeImageListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeImageListResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.next_token = next_token
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
                temp_model = DescribeImageListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageListResponseBody = None,
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
            temp_model = DescribeImageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        invocation_id: str = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids
        # This parameter is required.
        self.invocation_id = invocation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        return self


class DescribeInvocationsResponseBodyData(TeaModel):
    def __init__(
        self,
        finish_time: str = None,
        instance_id: str = None,
        invocation_id: str = None,
        invocation_status: str = None,
        output: str = None,
        start_time: str = None,
    ):
        self.finish_time = finish_time
        self.instance_id = instance_id
        self.invocation_id = invocation_id
        self.invocation_status = invocation_status
        self.output = output
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeInvocationsResponseBodyData] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.data = data
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
                temp_model = DescribeInvocationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvocationsResponseBody = None,
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
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeyPairsRequest(TeaModel):
    def __init__(
        self,
        key_pair_ids: List[str] = None,
        key_pair_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.key_pair_ids = key_pair_ids
        self.key_pair_name = key_pair_name
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_ids is not None:
            result['KeyPairIds'] = self.key_pair_ids
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairIds') is not None:
            self.key_pair_ids = m.get('KeyPairIds')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeKeyPairsResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        self.gmt_created = gmt_created
        self.key_pair_id = key_pair_id
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class DescribeKeyPairsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeKeyPairsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.next_token = next_token
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
                temp_model = DescribeKeyPairsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeyPairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKeyPairsResponseBody = None,
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
            temp_model = DescribeKeyPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionModels(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        region_models: List[DescribeRegionsResponseBodyRegionModels] = None,
        request_id: str = None,
    ):
        self.region_models = region_models
        self.request_id = request_id

    def validate(self):
        if self.region_models:
            for k in self.region_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModels'] = []
        if self.region_models is not None:
            for k in self.region_models:
                result['RegionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k in m.get('RegionModels'):
                temp_model = DescribeRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k))
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


class DescribeSpecRequest(TeaModel):
    def __init__(
        self,
        biz_region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        spec_ids: List[str] = None,
        spec_status: str = None,
        spec_type: str = None,
    ):
        self.biz_region_id = biz_region_id
        self.max_results = max_results
        self.next_token = next_token
        self.spec_ids = spec_ids
        self.spec_status = spec_status
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.spec_ids is not None:
            result['SpecIds'] = self.spec_ids
        if self.spec_status is not None:
            result['SpecStatus'] = self.spec_status
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SpecIds') is not None:
            self.spec_ids = m.get('SpecIds')
        if m.get('SpecStatus') is not None:
            self.spec_status = m.get('SpecStatus')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        return self


class DescribeSpecResponseBodySpecInfoModel(TeaModel):
    def __init__(
        self,
        core: int = None,
        memory: int = None,
        spec_id: str = None,
        spec_status: str = None,
        spec_type: str = None,
        system_disk_size: int = None,
    ):
        self.core = core
        self.memory = memory
        self.spec_id = spec_id
        self.spec_status = spec_status
        self.spec_type = spec_type
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core is not None:
            result['Core'] = self.core
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.spec_status is not None:
            result['SpecStatus'] = self.spec_status
        if self.spec_type is not None:
            result['SpecType'] = self.spec_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('SpecStatus') is not None:
            self.spec_status = m.get('SpecStatus')
        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeSpecResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        spec_info_model: List[DescribeSpecResponseBodySpecInfoModel] = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.spec_info_model = spec_info_model
        self.total_count = total_count

    def validate(self):
        if self.spec_info_model:
            for k in self.spec_info_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpecInfoModel'] = []
        if self.spec_info_model is not None:
            for k in self.spec_info_model:
                result['SpecInfoModel'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spec_info_model = []
        if m.get('SpecInfoModel') is not None:
            for k in m.get('SpecInfoModel'):
                temp_model = DescribeSpecResponseBodySpecInfoModel()
                self.spec_info_model.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSpecResponseBody = None,
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
            temp_model = DescribeSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        task_ids: List[str] = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.invoke_id = invoke_id
        self.max_results = max_results
        self.next_token = next_token
        self.resource_ids = resource_ids
        self.task_ids = task_ids
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        finish_time: str = None,
        invoke_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        result: str = None,
        start_time: str = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.finish_time = finish_time
        self.invoke_id = invoke_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.result = result
        self.start_time = start_time
        self.task_id = task_id
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.result is not None:
            result['Result'] = self.result
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeTasksResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.next_token = next_token
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
                temp_model = DescribeTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachKeyPairRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        key_pair_id: str = None,
    ):
        self.instance_ids = instance_ids
        # This parameter is required.
        self.key_pair_id = key_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        return self


class DetachKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        detached_instance_ids: List[str] = None,
        fail_count: int = None,
        key_pair_id: str = None,
        total_count: int = None,
    ):
        self.detached_instance_ids = detached_instance_ids
        self.fail_count = fail_count
        self.key_pair_id = key_pair_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detached_instance_ids is not None:
            result['DetachedInstanceIds'] = self.detached_instance_ids
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetachedInstanceIds') is not None:
            self.detached_instance_ids = m.get('DetachedInstanceIds')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DetachKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: DetachKeyPairResponseBodyData = None,
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
            temp_model = DetachKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachKeyPairResponseBody = None,
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
            temp_model = DetachKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DistributeImageRequest(TeaModel):
    def __init__(
        self,
        distribute_region_list: List[str] = None,
        image_id: str = None,
    ):
        # This parameter is required.
        self.distribute_region_list = distribute_region_list
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribute_region_list is not None:
            result['DistributeRegionList'] = self.distribute_region_list
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeRegionList') is not None:
            self.distribute_region_list = m.get('DistributeRegionList')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DistributeImageResponseBody(TeaModel):
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


class DistributeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DistributeImageResponseBody = None,
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
            temp_model = DistributeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DowngradeAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        auto_pay: bool = None,
        instance_group_id: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.auto_pay = auto_pay
        # This parameter is required.
        self.instance_group_id = instance_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        return self


class DowngradeAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DowngradeAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DowngradeAndroidInstanceGroupResponseBody = None,
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
            temp_model = DowngradeAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        source_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # This parameter is required.
        self.source_file_path = source_file_path
        # This parameter is required.
        self.upload_endpoint = upload_endpoint
        # This parameter is required.
        self.upload_type = upload_type
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        return self


class FetchFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FetchFileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[FetchFileResponseBodyData] = None,
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
                temp_model = FetchFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FetchFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchFileResponseBody = None,
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
            temp_model = FetchFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(
        self,
        key_pair_name: str = None,
        public_key_body: str = None,
    ):
        # This parameter is required.
        self.key_pair_name = key_pair_name
        # This parameter is required.
        self.public_key_body = public_key_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.public_key_body is not None:
            result['PublicKeyBody'] = self.public_key_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PublicKeyBody') is not None:
            self.public_key_body = m.get('PublicKeyBody')
        return self


class ImportKeyPairResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        self.gmt_created = gmt_created
        self.key_pair_id = key_pair_id
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        return self


class ImportKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        data: ImportKeyPairResponseBodyData = None,
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
            temp_model = ImportKeyPairResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportKeyPairResponseBody = None,
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
            temp_model = ImportKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallAppRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        instance_group_id_list: List[str] = None,
        instance_id_list: List[str] = None,
    ):
        self.app_id_list = app_id_list
        self.instance_group_id_list = instance_group_id_list
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.instance_group_id_list is not None:
            result['InstanceGroupIdList'] = self.instance_group_id_list
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('InstanceGroupIdList') is not None:
            self.instance_group_id_list = m.get('InstanceGroupIdList')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        return self


class InstallAppResponseBody(TeaModel):
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


class InstallAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallAppResponseBody = None,
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
            temp_model = InstallAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_group_ids: List[str] = None,
        policy_group_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.policy_group_ids = policy_group_ids
        self.policy_group_name = policy_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy(TeaModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
    ):
        self.custom_proxy = custom_proxy
        self.host_addr = host_addr
        self.net_redirect = net_redirect
        self.port = port
        self.proxy_password = proxy_password
        self.proxy_type = proxy_type
        self.proxy_user_name = proxy_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy
        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')
        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')
        return self


class ListPolicyGroupsResponseBodyPolicyGroupModel(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        gmt_create: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        session_resolution_height: str = None,
        session_resolution_width: str = None,
    ):
        self.camera_redirect = camera_redirect
        self.clipboard = clipboard
        self.gmt_create = gmt_create
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.lock_resolution = lock_resolution
        self.net_redirect_policy = net_redirect_policy
        self.policy_group_id = policy_group_id
        self.policy_group_name = policy_group_name
        self.session_resolution_height = session_resolution_height
        self.session_resolution_width = session_resolution_width

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            temp_model = ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m['NetRedirectPolicy'])
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        return self


class ListPolicyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        policy_group_model: List[ListPolicyGroupsResponseBodyPolicyGroupModel] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.next_token = next_token
        self.policy_group_model = policy_group_model
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.policy_group_model:
            for k in self.policy_group_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PolicyGroupModel'] = []
        if self.policy_group_model is not None:
            for k in self.policy_group_model:
                result['PolicyGroupModel'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policy_group_model = []
        if m.get('PolicyGroupModel') is not None:
            for k in m.get('PolicyGroupModel'):
                temp_model = ListPolicyGroupsResponseBodyPolicyGroupModel()
                self.policy_group_model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyGroupsResponseBody = None,
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
            temp_model = ListPolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        new_android_instance_name: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.new_android_instance_name = new_android_instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.new_android_instance_name is not None:
            result['NewAndroidInstanceName'] = self.new_android_instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('NewAndroidInstanceName') is not None:
            self.new_android_instance_name = m.get('NewAndroidInstanceName')
        return self


class ModifyAndroidInstanceResponseBody(TeaModel):
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


class ModifyAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAndroidInstanceResponseBody = None,
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
            temp_model = ModifyAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        instance_group_id: str = None,
        new_instance_group_name: str = None,
        policy_group_id: str = None,
    ):
        self.instance_group_id = instance_group_id
        self.new_instance_group_name = new_instance_group_name
        self.policy_group_id = policy_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        if self.new_instance_group_name is not None:
            result['NewInstanceGroupName'] = self.new_instance_group_name
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        if m.get('NewInstanceGroupName') is not None:
            self.new_instance_group_name = m.get('NewInstanceGroupName')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class ModifyAndroidInstanceGroupResponseBody(TeaModel):
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


class ModifyAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAndroidInstanceGroupResponseBody = None,
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
            temp_model = ModifyAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
        icon_url: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.description = description
        self.icon_url = icon_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        return self


class ModifyAppResponseBody(TeaModel):
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


class ModifyAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppResponseBody = None,
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyKeyPairNameRequest(TeaModel):
    def __init__(
        self,
        key_pair_id: str = None,
        new_key_pair_name: str = None,
    ):
        # This parameter is required.
        self.key_pair_id = key_pair_id
        # This parameter is required.
        self.new_key_pair_name = new_key_pair_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id
        if self.new_key_pair_name is not None:
            result['NewKeyPairName'] = self.new_key_pair_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')
        if m.get('NewKeyPairName') is not None:
            self.new_key_pair_name = m.get('NewKeyPairName')
        return self


class ModifyKeyPairNameResponseBody(TeaModel):
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


class ModifyKeyPairNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyKeyPairNameResponseBody = None,
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
            temp_model = ModifyKeyPairNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyGroupRequestNetRedirectPolicy(TeaModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
    ):
        self.custom_proxy = custom_proxy
        self.host_addr = host_addr
        self.net_redirect = net_redirect
        self.port = port
        self.proxy_password = proxy_password
        self.proxy_type = proxy_type
        self.proxy_user_name = proxy_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy
        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.port is not None:
            result['Port'] = self.port
        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')
        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')
        return self


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: ModifyPolicyGroupRequestNetRedirectPolicy = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.camera_redirect = camera_redirect
        self.clipboard = clipboard
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.lock_resolution = lock_resolution
        self.net_redirect_policy = net_redirect_policy
        self.policy_group_id = policy_group_id
        self.policy_group_name = policy_group_name
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            temp_model = ModifyPolicyGroupRequestNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m['NetRedirectPolicy'])
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class ModifyPolicyGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy_shrink: str = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.camera_redirect = camera_redirect
        self.clipboard = clipboard
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.lock_resolution = lock_resolution
        self.net_redirect_policy_shrink = net_redirect_policy_shrink
        self.policy_group_id = policy_group_id
        self.policy_group_name = policy_group_name
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution
        if self.net_redirect_policy_shrink is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy_shrink
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height
        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')
        if m.get('NetRedirectPolicy') is not None:
            self.net_redirect_policy_shrink = m.get('NetRedirectPolicy')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')
        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')
        return self


class ModifyPolicyGroupResponseBody(TeaModel):
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


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyGroupResponseBody = None,
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
            temp_model = ModifyPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootAndroidInstancesInGroupRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        force_stop: bool = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.force_stop = force_stop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        return self


class RebootAndroidInstancesInGroupResponseBody(TeaModel):
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


class RebootAndroidInstancesInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootAndroidInstancesInGroupResponseBody = None,
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
            temp_model = RebootAndroidInstancesInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        backup_file_id: str = None,
        backup_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
    ):
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        self.backup_file_id = backup_file_id
        self.backup_file_path = backup_file_path
        self.upload_endpoint = upload_endpoint
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.backup_file_id is not None:
            result['BackupFileId'] = self.backup_file_id
        if self.backup_file_path is not None:
            result['BackupFilePath'] = self.backup_file_path
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('BackupFileId') is not None:
            self.backup_file_id = m.get('BackupFileId')
        if m.get('BackupFilePath') is not None:
            self.backup_file_path = m.get('BackupFilePath')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class RecoveryFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RecoveryFileResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        data: List[RecoveryFileResponseBodyData] = None,
        request_id: str = None,
    ):
        self.count = count
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
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = RecoveryFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecoveryFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoveryFileResponseBody = None,
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
            temp_model = RecoveryFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAndroidInstanceGroupsRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_group_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
    ):
        self.auto_pay = auto_pay
        self.instance_group_ids = instance_group_ids
        self.period = period
        self.period_unit = period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        return self


class RenewAndroidInstanceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewAndroidInstanceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewAndroidInstanceGroupsResponseBody = None,
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
            temp_model = RenewAndroidInstanceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAndroidInstancesInGroupRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
    ):
        self.android_instance_ids = android_instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        return self


class ResetAndroidInstancesInGroupResponseBody(TeaModel):
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


class ResetAndroidInstancesInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAndroidInstancesInGroupResponseBody = None,
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
            temp_model = ResetAndroidInstancesInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        content_encoding: str = None,
        instance_ids: List[str] = None,
        timeout: int = None,
    ):
        self.command_content = command_content
        self.content_encoding = content_encoding
        self.instance_ids = instance_ids
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCommandResponseBody = None,
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
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendFileRequest(TeaModel):
    def __init__(
        self,
        android_instance_id_list: List[str] = None,
        source_file_path: str = None,
        upload_endpoint: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        # This parameter is required.
        self.android_instance_id_list = android_instance_id_list
        # This parameter is required.
        self.source_file_path = source_file_path
        # This parameter is required.
        self.upload_endpoint = upload_endpoint
        # This parameter is required.
        self.upload_type = upload_type
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id_list is not None:
            result['AndroidInstanceIdList'] = self.android_instance_id_list
        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path
        if self.upload_endpoint is not None:
            result['UploadEndpoint'] = self.upload_endpoint
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIdList') is not None:
            self.android_instance_id_list = m.get('AndroidInstanceIdList')
        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')
        if m.get('UploadEndpoint') is not None:
            self.upload_endpoint = m.get('UploadEndpoint')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        return self


class SendFileResponseBodyData(TeaModel):
    def __init__(
        self,
        android_instance_id: str = None,
        task_id: str = None,
    ):
        self.android_instance_id = android_instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SendFileResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SendFileResponseBodyData] = None,
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
                temp_model = SendFileResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendFileResponseBody = None,
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
            temp_model = SendFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
    ):
        self.android_instance_ids = android_instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        return self


class StartAndroidInstanceResponseBody(TeaModel):
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


class StartAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAndroidInstanceResponseBody = None,
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
            temp_model = StartAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAndroidInstanceRequest(TeaModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        force_stop: bool = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.force_stop = force_stop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        return self


class StopAndroidInstanceResponseBody(TeaModel):
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


class StopAndroidInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAndroidInstanceResponseBody = None,
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
            temp_model = StopAndroidInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallAppRequest(TeaModel):
    def __init__(
        self,
        app_id_list: List[str] = None,
        instance_group_id_list: List[str] = None,
    ):
        self.app_id_list = app_id_list
        self.instance_group_id_list = instance_group_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id_list is not None:
            result['AppIdList'] = self.app_id_list
        if self.instance_group_id_list is not None:
            result['InstanceGroupIdList'] = self.instance_group_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdList') is not None:
            self.app_id_list = m.get('AppIdList')
        if m.get('InstanceGroupIdList') is not None:
            self.instance_group_id_list = m.get('InstanceGroupIdList')
        return self


class UninstallAppResponseBody(TeaModel):
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


class UninstallAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallAppResponseBody = None,
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
            temp_model = UninstallAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomImageNameRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        return self


class UpdateCustomImageNameResponseBody(TeaModel):
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


class UpdateCustomImageNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomImageNameResponseBody = None,
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
            temp_model = UpdateCustomImageNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceGroupImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_group_ids: List[str] = None,
    ):
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.instance_group_ids = instance_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')
        return self


class UpdateInstanceGroupImageResponseBody(TeaModel):
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


class UpdateInstanceGroupImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceGroupImageResponseBody = None,
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
            temp_model = UpdateInstanceGroupImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeAndroidInstanceGroupRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        increase_number_of_instance: int = None,
        instance_group_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.increase_number_of_instance = increase_number_of_instance
        self.instance_group_id = instance_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.increase_number_of_instance is not None:
            result['IncreaseNumberOfInstance'] = self.increase_number_of_instance
        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('IncreaseNumberOfInstance') is not None:
            self.increase_number_of_instance = m.get('IncreaseNumberOfInstance')
        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')
        return self


class UpgradeAndroidInstanceGroupResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.order_id = order_id
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeAndroidInstanceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeAndroidInstanceGroupResponseBody = None,
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
            temp_model = UpgradeAndroidInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


