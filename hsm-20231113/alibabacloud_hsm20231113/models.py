# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ConfigAuditLogRequest(TeaModel):
    def __init__(
        self,
        audit_action: str = None,
        audit_oss_bucket: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable the audit log feature. Valid values:
        # 
        # *   enable
        # *   disable
        # 
        # This parameter is required.
        self.audit_action = audit_action
        # The bucket to which audit logs are delivered.
        self.audit_oss_bucket = audit_oss_bucket
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_action is not None:
            result['AuditAction'] = self.audit_action
        if self.audit_oss_bucket is not None:
            result['AuditOssBucket'] = self.audit_oss_bucket
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditAction') is not None:
            self.audit_action = m.get('AuditAction')
        if m.get('AuditOssBucket') is not None:
            self.audit_oss_bucket = m.get('AuditOssBucket')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigAuditLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigAuditLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigAuditLogResponseBody = None,
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
            temp_model = ConfigAuditLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigBackupRemarkRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        name: str = None,
        remark: str = None,
    ):
        # The ID of the backup.
        # 
        # This parameter is required.
        self.backup_id = backup_id
        # The name of the backup.
        self.name = name
        # The description of the backup.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ConfigBackupRemarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigBackupRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigBackupRemarkResponseBody = None,
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
            temp_model = ConfigBackupRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigBackupTaskRequest(TeaModel):
    def __init__(
        self,
        backup_hour_in_day: int = None,
        backup_id: str = None,
        backup_period: int = None,
        manual_2periodic_list: List[str] = None,
        periodic_2manual_list: List[str] = None,
    ):
        # The backup time in the 24-hour format. Valid values: 1 to 24.
        # 
        # Enumeration values:
        # 
        # *   0
        # *   1
        # *   2
        # *   3
        # *   4
        # *   5
        # *   6
        # *   7
        # *   8
        # *   9
        # *   10
        # *   11
        # *   12
        # *   13
        # *   14
        # *   15
        # *   16
        # *   17
        # *   18
        # *   19
        # *   20
        # *   21
        # *   22
        # *   23
        # 
        # This parameter is required.
        self.backup_hour_in_day = backup_hour_in_day
        # The ID of the backup.
        # 
        # This parameter is required.
        self.backup_id = backup_id
        # The automatic backup cycle. Unit: days. Valid values: 1, 3, 7, and 30.
        # 
        # This parameter is required.
        self.backup_period = backup_period
        # The IDs of images for which the manual backup mode is updated to the automatic backup mode.
        self.manual_2periodic_list = manual_2periodic_list
        # The IDs of images for which the automatic backup mode is updated to the manual backup mode.
        self.periodic_2manual_list = periodic_2manual_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_hour_in_day is not None:
            result['BackupHourInDay'] = self.backup_hour_in_day
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.manual_2periodic_list is not None:
            result['Manual2PeriodicList'] = self.manual_2periodic_list
        if self.periodic_2manual_list is not None:
            result['Periodic2ManualList'] = self.periodic_2manual_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupHourInDay') is not None:
            self.backup_hour_in_day = m.get('BackupHourInDay')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('Manual2PeriodicList') is not None:
            self.manual_2periodic_list = m.get('Manual2PeriodicList')
        if m.get('Periodic2ManualList') is not None:
            self.periodic_2manual_list = m.get('Periodic2ManualList')
        return self


class ConfigBackupTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigBackupTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigBackupTaskResponseBody = None,
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
            temp_model = ConfigBackupTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigClusterCertificateRequest(TeaModel):
    def __init__(
        self,
        cluster_certificate: str = None,
        cluster_id: str = None,
        issuer_certificate: str = None,
    ):
        # The cluster certificate.
        # 
        # This parameter is required.
        self.cluster_certificate = cluster_certificate
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The self-signed certificate.
        # 
        # This parameter is required.
        self.issuer_certificate = issuer_certificate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_certificate is not None:
            result['ClusterCertificate'] = self.cluster_certificate
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.issuer_certificate is not None:
            result['IssuerCertificate'] = self.issuer_certificate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCertificate') is not None:
            self.cluster_certificate = m.get('ClusterCertificate')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IssuerCertificate') is not None:
            self.issuer_certificate = m.get('IssuerCertificate')
        return self


class ConfigClusterCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigClusterCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigClusterCertificateResponseBody = None,
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
            temp_model = ConfigClusterCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ConfigClusterNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigClusterNameResponseBody = None,
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
            temp_model = ConfigClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigClusterSubnetRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The ID of the cluster. You can call the ListCluster operation to obtain cluster IDs.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # A list of vSwitches that are associated with the cluster. Note: You must include all vSwitches that you want to associate with the cluster.
        # 
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ConfigClusterSubnetShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        v_switch_ids_shrink: str = None,
        vpc_id: str = None,
    ):
        # The ID of the cluster. You can call the ListCluster operation to obtain cluster IDs.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # A list of vSwitches that are associated with the cluster. Note: You must include all vSwitches that you want to associate with the cluster.
        # 
        # This parameter is required.
        self.v_switch_ids_shrink = v_switch_ids_shrink
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ConfigClusterSubnetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigClusterSubnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigClusterSubnetResponseBody = None,
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
            temp_model = ConfigClusterSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigClusterWhitelistRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        whitelist: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The IP address whitelist of the cluster.
        # 
        # This parameter is required.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ConfigClusterWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigClusterWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigClusterWhitelistResponseBody = None,
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
            temp_model = ConfigClusterWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigImageRemarkRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        remark: str = None,
    ):
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The description of the image.
        # 
        # This parameter is required.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ConfigImageRemarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigImageRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigImageRemarkResponseBody = None,
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
            temp_model = ConfigImageRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceIpAddressRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The endpoint of the VPC to which the HMS belongs.
        # 
        # This parameter is required.
        self.ip = ip
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the vSwitch to which the HMS belongs.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the HMS belongs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ConfigInstanceIpAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigInstanceIpAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigInstanceIpAddressResponseBody = None,
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
            temp_model = ConfigInstanceIpAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceRemarkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        remark: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The description of the HSM.
        # 
        # This parameter is required.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ConfigInstanceRemarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigInstanceRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigInstanceRemarkResponseBody = None,
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
            temp_model = ConfigInstanceRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhitelistRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        whitelist: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # A list of IP addresses that you want to configure in the whitelist. Separate multiple IP addresses with spaces or commas (,).
        # 
        # This parameter is required.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ConfigInstanceWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ConfigInstanceWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigInstanceWhitelistResponseBody = None,
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
            temp_model = ConfigInstanceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyImageRequest(TeaModel):
    def __init__(
        self,
        image_uid: str = None,
        target_region_id: str = None,
    ):
        # The ID of the image.
        self.image_uid = image_uid
        # The ID of the destination region.
        self.target_region_id = target_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uid is not None:
            result['ImageUid'] = self.image_uid
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUid') is not None:
            self.image_uid = m.get('ImageUid')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        return self


class CopyImageResponseBody(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete.
        self.completed = completed
        # The time when the task is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.create_time = create_time
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The response returned after the task succeeds.
        self.response = response
        # The task status.
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CopyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyImageResponseBody = None,
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
            temp_model = CopyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        master_instance_id: str = None,
        region_id: str = None,
    ):
        # The name of the cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The ID of the master HSM.
        # 
        # This parameter is required.
        self.master_instance_id = master_instance_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
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


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The language of the content. Valid values:
        # 
        # *   zh: Chinese.
        # *   en: English.
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


class DescribeRegionsResponseBodyRegionsZones(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        local_name: str = None,
        zone_id: str = None,
    ):
        # Indicates whether clusters are supported. Valid values:
        # 
        # *   yes
        # *   no
        self.cluster = cluster
        # The name of the zone.
        self.local_name = local_name
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
        zones: List[DescribeRegionsResponseBodyRegionsZones] = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The region ID.
        self.region_id = region_id
        # The zones.
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
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeRegionsResponseBodyRegionsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
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


class DownloadClusterManagedCertRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DownloadClusterManagedCertResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
    ):
        self.content = content
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DownloadClusterManagedCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadClusterManagedCertResponseBody = None,
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
            temp_model = DownloadClusterManagedCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBackupRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the backup.
        # 
        # This parameter is required.
        self.backup_id = backup_id
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableBackupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class EnableBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableBackupResponseBody = None,
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
            temp_model = EnableBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ExportImageResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        error: str = None,
        job_id: str = None,
        process: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete. Valid values:
        # 
        # *   true
        # *   false
        self.completed = completed
        # The error message returned if the operation is abnormal or fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.process = process
        # The response returned after the operation succeeds.
        self.response = response
        # The task status. Valid values:
        # 
        # *   running
        # *   cancel
        # *   fail
        # *   success
        self.status = status
        # The type of the task operation. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.process is not None:
            result['Process'] = self.process
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ExportImageResponseBody(TeaModel):
    def __init__(
        self,
        job: ExportImageResponseBodyJob = None,
        request_id: str = None,
    ):
        # The information about the asynchronous task returned.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = ExportImageResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportImageResponseBody = None,
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
            temp_model = ExportImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditLogStatusRequest(TeaModel):
    def __init__(
        self,
        get_oss_bucket: bool = None,
        region_id: str = None,
    ):
        # Specifies whether to obtain the list of OSS buckets that can be used to store audit logs. Valid values:
        # 
        # *   true
        # *   false
        self.get_oss_bucket = get_oss_bucket
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_oss_bucket is not None:
            result['GetOssBucket'] = self.get_oss_bucket
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetOssBucket') is not None:
            self.get_oss_bucket = m.get('GetOssBucket')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAuditLogStatusResponseBody(TeaModel):
    def __init__(
        self,
        audit_log_status: str = None,
        audit_oss_bucket: str = None,
        granted_service_access: bool = None,
        oss_buckets: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Indicates whether the audit log feature is enabled. Valid values:
        # 
        # *   enable
        # *   disable
        self.audit_log_status = audit_log_status
        # The bucket that stores audit logs.
        self.audit_oss_bucket = audit_oss_bucket
        # Indicates whether Cloud Hardware Security Module is authorized to deliver logs. Valid values:
        # 
        # *   true
        # *   false
        self.granted_service_access = granted_service_access
        # A list of buckets that can be used to store audit logs.
        self.oss_buckets = oss_buckets
        # The ID of the region.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status
        if self.audit_oss_bucket is not None:
            result['AuditOssBucket'] = self.audit_oss_bucket
        if self.granted_service_access is not None:
            result['GrantedServiceAccess'] = self.granted_service_access
        if self.oss_buckets is not None:
            result['OssBuckets'] = self.oss_buckets
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')
        if m.get('AuditOssBucket') is not None:
            self.audit_oss_bucket = m.get('AuditOssBucket')
        if m.get('GrantedServiceAccess') is not None:
            self.granted_service_access = m.get('GrantedServiceAccess')
        if m.get('OssBuckets') is not None:
            self.oss_buckets = m.get('OssBuckets')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAuditLogStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuditLogStatusResponseBody = None,
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
            temp_model = GetAuditLogStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBackupRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class GetBackupResponseBodyBackup(TeaModel):
    def __init__(
        self,
        auto_image_count: int = None,
        backup_hour_in_day: str = None,
        backup_id: str = None,
        backup_period: int = None,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        max_image_count: str = None,
        name: str = None,
        next_image_create_time: int = None,
        owner_instance_id: str = None,
        region_id: str = None,
        release_time: int = None,
        remark: str = None,
        sp_instance_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The number of images that are automatically backed up.
        self.auto_image_count = auto_image_count
        # The backup time in the 24-hour format.
        self.backup_hour_in_day = backup_hour_in_day
        # The ID of the backup.
        self.backup_id = backup_id
        # The automatic backup cycle. Unit: days.
        self.backup_period = backup_period
        # The time when the backup is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.create_time = create_time
        # The expiration time of the backup. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.expire_time = expire_time
        # The ID of the hardware security module (HSM) that is associated with the backup.
        self.instance_id = instance_id
        # The maximum number of images.
        self.max_image_count = max_image_count
        # The name of the backup.
        self.name = name
        # The next time when the image is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.next_image_create_time = next_image_create_time
        # The ID of the HSM to which the backup belongs. This parameter is available only for HSM backups outside the Chinese mainland and the value of this parameter is consistent with the value of InstanceId.
        self.owner_instance_id = owner_instance_id
        # The ID of the region.
        self.region_id = region_id
        # The time when the backup is released. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.release_time = release_time
        # The description of the backup.
        self.remark = remark
        # The ID of the backup. This parameter is available only for HSM backups in the Chinese mainland.
        self.sp_instance_id = sp_instance_id
        # The status of the backup. Valid values:
        # 
        # *   NEW
        # *   EXPIRED
        # *   ENABLED
        self.status = status
        # The type of the backup. Valid values:
        # 
        # *   DEFAULT
        # *   NORMAL
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_image_count is not None:
            result['AutoImageCount'] = self.auto_image_count
        if self.backup_hour_in_day is not None:
            result['BackupHourInDay'] = self.backup_hour_in_day
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_image_count is not None:
            result['MaxImageCount'] = self.max_image_count
        if self.name is not None:
            result['Name'] = self.name
        if self.next_image_create_time is not None:
            result['NextImageCreateTime'] = self.next_image_create_time
        if self.owner_instance_id is not None:
            result['OwnerInstanceId'] = self.owner_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sp_instance_id is not None:
            result['SpInstanceId'] = self.sp_instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoImageCount') is not None:
            self.auto_image_count = m.get('AutoImageCount')
        if m.get('BackupHourInDay') is not None:
            self.backup_hour_in_day = m.get('BackupHourInDay')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxImageCount') is not None:
            self.max_image_count = m.get('MaxImageCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextImageCreateTime') is not None:
            self.next_image_create_time = m.get('NextImageCreateTime')
        if m.get('OwnerInstanceId') is not None:
            self.owner_instance_id = m.get('OwnerInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SpInstanceId') is not None:
            self.sp_instance_id = m.get('SpInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetBackupResponseBody(TeaModel):
    def __init__(
        self,
        backup: GetBackupResponseBodyBackup = None,
        request_id: str = None,
    ):
        # The information about the backup.
        self.backup = backup
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.backup:
            self.backup.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup is not None:
            result['Backup'] = self.backup.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Backup') is not None:
            temp_model = GetBackupResponseBodyBackup()
            self.backup = temp_model.from_map(m['Backup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBackupResponseBody = None,
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
            temp_model = GetBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetClusterResponseBodyClusterInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        master: bool = None,
        node_id: int = None,
    ):
        # The ID of the HSM.
        self.instance_id = instance_id
        # Indicates whether the HSM is a master HSM. Valid values:
        # 
        # *   true
        # *   false
        self.master = master
        # The ID of the HSM in the cluster.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.master is not None:
            result['Master'] = self.master
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Master') is not None:
            self.master = m.get('Master')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class GetClusterResponseBodyClusterZones(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetClusterResponseBodyCluster(TeaModel):
    def __init__(
        self,
        cert_managed: bool = None,
        cluster_certificate: str = None,
        cluster_csr: str = None,
        cluster_id: str = None,
        cluster_mode: int = None,
        cluster_name: str = None,
        cluster_owner_certificate: str = None,
        create_time: int = None,
        device_type: str = None,
        entity_cert_expire_time: str = None,
        instances: List[GetClusterResponseBodyClusterInstances] = None,
        region_id: str = None,
        size: int = None,
        status: str = None,
        vpc_id: str = None,
        whitelist: str = None,
        zones: List[GetClusterResponseBodyClusterZones] = None,
    ):
        self.cert_managed = cert_managed
        # The cluster certificate.
        self.cluster_certificate = cluster_certificate
        # The certificate signing request (CSR) file of the cluster.
        self.cluster_csr = cluster_csr
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The cluster mode.
        # 
        # 2: automatically synchronizes the cluster.
        self.cluster_mode = cluster_mode
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The self-signed certificate of the cluster.
        self.cluster_owner_certificate = cluster_owner_certificate
        # The time when the cluster was created. Unit: milliseconds. The value is a UNIX timestamp.
        self.create_time = create_time
        # The type of the device.
        self.device_type = device_type
        self.entity_cert_expire_time = entity_cert_expire_time
        # The HSMs in the cluster.
        self.instances = instances
        # The ID of the region in which the cluster resides.
        self.region_id = region_id
        # The number of hardware security modules (HSMs) in the cluster.
        self.size = size
        # The status of the cluster. Valid values:
        # 
        # *   NEW: The cluster is not initialized.
        # *   INITIALIZED: The cluster is initialized.
        # *   DELETED: The cluster is deleted.
        # *   SYNCHRONIZING: The cluster is being synchronized.
        # *   TO_DELETE: The cluster is pending deletion.
        self.status = status
        # The ID of the virtual private cloud (VPC) to which the cluster belongs.
        self.vpc_id = vpc_id
        # The IP address whitelist of the cluster.
        self.whitelist = whitelist
        # The information about the zones in which the cluster is deployed.
        self.zones = zones

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_managed is not None:
            result['CertManaged'] = self.cert_managed
        if self.cluster_certificate is not None:
            result['ClusterCertificate'] = self.cluster_certificate
        if self.cluster_csr is not None:
            result['ClusterCsr'] = self.cluster_csr
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_mode is not None:
            result['ClusterMode'] = self.cluster_mode
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_owner_certificate is not None:
            result['ClusterOwnerCertificate'] = self.cluster_owner_certificate
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.entity_cert_expire_time is not None:
            result['EntityCertExpireTime'] = self.entity_cert_expire_time
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertManaged') is not None:
            self.cert_managed = m.get('CertManaged')
        if m.get('ClusterCertificate') is not None:
            self.cluster_certificate = m.get('ClusterCertificate')
        if m.get('ClusterCsr') is not None:
            self.cluster_csr = m.get('ClusterCsr')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterMode') is not None:
            self.cluster_mode = m.get('ClusterMode')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterOwnerCertificate') is not None:
            self.cluster_owner_certificate = m.get('ClusterOwnerCertificate')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EntityCertExpireTime') is not None:
            self.entity_cert_expire_time = m.get('EntityCertExpireTime')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = GetClusterResponseBodyClusterInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = GetClusterResponseBodyClusterZones()
                self.zones.append(temp_model.from_map(k))
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster: GetClusterResponseBodyCluster = None,
        request_id: str = None,
    ):
        # The cluster details.
        self.cluster = cluster
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = GetClusterResponseBodyCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterResponseBody = None,
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
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class GetImageResponseBodyImage(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        copy_time: int = None,
        export_time: int = None,
        image_id: str = None,
        instance_id: str = None,
        mode: str = None,
        region_id: str = None,
        remark: str = None,
        source_backup_uid: str = None,
        source_image_uid: str = None,
        source_instance_id: str = None,
        source_region_id: str = None,
        status: str = None,
        vsm_digest: str = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id
        # The time when the image was copied. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.copy_time = copy_time
        # The time when the image was generated. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.export_time = export_time
        # The ID of the image.
        self.image_id = image_id
        # The ID of the hardware security module (HSM).
        self.instance_id = instance_id
        # The image generation mode. Valid values:
        # 
        # *   PERIODIC
        # *   MANUAL
        self.mode = mode
        # The ID of the region.
        self.region_id = region_id
        # The description of the backup.
        self.remark = remark
        # The ID of the source backup.
        self.source_backup_uid = source_backup_uid
        # The ID of the source image.
        self.source_image_uid = source_image_uid
        # The ID of the source HSM.
        self.source_instance_id = source_instance_id
        # The region ID of the source image.
        self.source_region_id = source_region_id
        # The status of the image. Valid values:
        # 
        # *   NEW
        # *   DELETED
        # *   CREATING
        # *   NORMAL
        self.status = status
        # The digest of the HSM.
        self.vsm_digest = vsm_digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.copy_time is not None:
            result['CopyTime'] = self.copy_time
        if self.export_time is not None:
            result['ExportTime'] = self.export_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source_backup_uid is not None:
            result['SourceBackupUid'] = self.source_backup_uid
        if self.source_image_uid is not None:
            result['SourceImageUid'] = self.source_image_uid
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vsm_digest is not None:
            result['VsmDigest'] = self.vsm_digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('CopyTime') is not None:
            self.copy_time = m.get('CopyTime')
        if m.get('ExportTime') is not None:
            self.export_time = m.get('ExportTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SourceBackupUid') is not None:
            self.source_backup_uid = m.get('SourceBackupUid')
        if m.get('SourceImageUid') is not None:
            self.source_image_uid = m.get('SourceImageUid')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VsmDigest') is not None:
            self.vsm_digest = m.get('VsmDigest')
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        image: GetImageResponseBodyImage = None,
        request_id: str = None,
    ):
        # The image information.
        self.image = image
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = GetImageResponseBodyImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageResponseBody = None,
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
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the HSM.
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


class GetInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        certification: str = None,
        certification_url: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: int = None,
        device_type: str = None,
        expire_time: int = None,
        instance_id: str = None,
        ip: str = None,
        is_trial: bool = None,
        master: bool = None,
        order_id: str = None,
        pqc_enabled: int = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        tenant_isolation_type: str = None,
        v_switch_id: str = None,
        vendor: str = None,
        vpc_id: str = None,
        whitelist: str = None,
        zone_id: str = None,
    ):
        self.certification = certification
        self.certification_url = certification_url
        # The ID of the cluster to which the HSM belongs.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The time when the HSM was created.
        self.create_time = create_time
        # The type of the device.
        self.device_type = device_type
        # The time when the HSM expired.
        self.expire_time = expire_time
        # The ID of the HSM.
        self.instance_id = instance_id
        # The IP address of the HSM in the VPC.
        self.ip = ip
        # Indicates whether the HSM is for trial use. Valid values:
        # 
        # *   true
        # *   false
        self.is_trial = is_trial
        # Indicates whether the HSM is a master HSM. Valid values:
        # 
        # *   true
        # *   false
        self.master = master
        # The ID of the order.
        self.order_id = order_id
        self.pqc_enabled = pqc_enabled
        # The ID of the region.
        self.region_id = region_id
        # The description of the HSM.
        self.remark = remark
        # The status of the HSM. Valid values:
        # 
        # *   PENDING: The HSM is disabled.
        # *   ACTIVE: The HSM is enabled.
        # *   EXPIRED: The HSM expired.
        # *   INVALID: The HSM is invalid.
        # *   FAILURE: The HSM failed to be created.
        # *   RESET: The HSM is being reset.
        # *   PAUSED: The HSM is paused.
        # *   MODIFYING: The HSM is being modified.
        self.status = status
        # The type of HSMs that is classified based on resource isolation. Valid values: 
        # - vsm: Virtual security modules (VSMs)
        # - hostedHsm: Dedicated HSMs.
        self.tenant_isolation_type = tenant_isolation_type
        # The ID of the vSwitch that is configured for the HSM.
        self.v_switch_id = v_switch_id
        # The information about the vendor.
        self.vendor = vendor
        # The ID of the virtual private cloud (VPC) to which the HSM belongs.
        self.vpc_id = vpc_id
        # The IP addresses in the whitelist.
        self.whitelist = whitelist
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certification is not None:
            result['Certification'] = self.certification
        if self.certification_url is not None:
            result['CertificationUrl'] = self.certification_url
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial
        if self.master is not None:
            result['Master'] = self.master
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pqc_enabled is not None:
            result['PqcEnabled'] = self.pqc_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_isolation_type is not None:
            result['TenantIsolationType'] = self.tenant_isolation_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certification') is not None:
            self.certification = m.get('Certification')
        if m.get('CertificationUrl') is not None:
            self.certification_url = m.get('CertificationUrl')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')
        if m.get('Master') is not None:
            self.master = m.get('Master')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PqcEnabled') is not None:
            self.pqc_enabled = m.get('PqcEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantIsolationType') is not None:
            self.tenant_isolation_type = m.get('TenantIsolationType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance: GetInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The information about the HSM.
        self.instance = instance
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The ID of the task.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete. Valid values:
        # 
        # *   true
        # *   false
        self.completed = completed
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The response returned after the task succeeds.
        self.response = response
        # The task status. Valid values:
        # 
        # *   success
        # *   running
        # *   fail
        # *   cancel
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        job: GetJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The details of the task.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = GetJobResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
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
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeAuditLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class InitializeAuditLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeAuditLogResponseBody = None,
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
            temp_model = InitializeAuditLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class InitializeClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class InitializeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitializeClusterResponseBody = None,
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
            temp_model = InitializeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the HSM that you want to add to the cluster.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class JoinClusterResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete. Valid values:
        # 
        # *   true
        # *   false
        self.completed = completed
        # The time when the task was created. Unit: milliseconds. The value is a UNIX timestamp.
        self.create_time = create_time
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The response returned after the task succeeds.
        self.response = response
        # The status of the task. Valid values:
        # 
        # *   success
        # *   running
        # *   cancel
        # *   fail
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class JoinClusterResponseBody(TeaModel):
    def __init__(
        self,
        job: JoinClusterResponseBodyJob = None,
        request_id: str = None,
    ):
        # The details of the task.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = JoinClusterResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JoinClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JoinClusterResponseBody = None,
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
            temp_model = JoinClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LeaveClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class LeaveClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class LeaveClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LeaveClusterResponseBody = None,
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
            temp_model = LeaveClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBackupsRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        current_page: int = None,
        instance_id: str = None,
        name: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The ID of the hardware security module (HSM).
        self.instance_id = instance_id
        # The name of the backup.
        self.name = name
        # The number of entries per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBackupsResponseBodyBackups(TeaModel):
    def __init__(
        self,
        auto_image_count: int = None,
        backup_hour_in_day: str = None,
        backup_id: str = None,
        backup_period: int = None,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        max_image_count: str = None,
        name: str = None,
        next_image_create_time: int = None,
        owner_instance_id: str = None,
        region_id: str = None,
        release_time: int = None,
        remark: str = None,
        sp_instance_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The number of images that are automatically backed up.
        self.auto_image_count = auto_image_count
        # The backup time on the hour that is in the 24-hour clock.
        self.backup_hour_in_day = backup_hour_in_day
        # The ID of the backup.
        self.backup_id = backup_id
        # The automatic backup cycle. Unit: days.
        self.backup_period = backup_period
        # The time when the backup is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.create_time = create_time
        # The expiration time of the backup. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.expire_time = expire_time
        # The ID of the HSM that is associated with the backup.
        self.instance_id = instance_id
        # The number of images.
        self.max_image_count = max_image_count
        # The name of the backup.
        self.name = name
        # The time when the image is created next time. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.next_image_create_time = next_image_create_time
        # The ID of the HSM to which the backup belongs. This parameter is available only for HSM backups outside the Chinese mainland and the value of this parameter is consistent with the value of InstanceId.
        self.owner_instance_id = owner_instance_id
        # The ID of the region.
        self.region_id = region_id
        # The time when the backup is released. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.release_time = release_time
        # The description of the backup.
        self.remark = remark
        # The ID of the backup. This parameter is available only for HSM backups in the Chinese mainland.
        self.sp_instance_id = sp_instance_id
        # The status of the backup. Valid values:
        # 
        # *   NEW: The backup is disabled.
        # *   EXPIRED: The backup expired.
        # *   ENABLED: The backup is enabled.
        self.status = status
        # The type of the backup. Valid values:
        # 
        # *   DEFAULT
        # *   NORMAL
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_image_count is not None:
            result['AutoImageCount'] = self.auto_image_count
        if self.backup_hour_in_day is not None:
            result['BackupHourInDay'] = self.backup_hour_in_day
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_image_count is not None:
            result['MaxImageCount'] = self.max_image_count
        if self.name is not None:
            result['Name'] = self.name
        if self.next_image_create_time is not None:
            result['NextImageCreateTime'] = self.next_image_create_time
        if self.owner_instance_id is not None:
            result['OwnerInstanceId'] = self.owner_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sp_instance_id is not None:
            result['SpInstanceId'] = self.sp_instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoImageCount') is not None:
            self.auto_image_count = m.get('AutoImageCount')
        if m.get('BackupHourInDay') is not None:
            self.backup_hour_in_day = m.get('BackupHourInDay')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxImageCount') is not None:
            self.max_image_count = m.get('MaxImageCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextImageCreateTime') is not None:
            self.next_image_create_time = m.get('NextImageCreateTime')
        if m.get('OwnerInstanceId') is not None:
            self.owner_instance_id = m.get('OwnerInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SpInstanceId') is not None:
            self.sp_instance_id = m.get('SpInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBackupsResponseBody(TeaModel):
    def __init__(
        self,
        backups: List[ListBackupsResponseBodyBackups] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The backups returned.
        self.backups = backups
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.backups:
            for k in self.backups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Backups'] = []
        if self.backups is not None:
            for k in self.backups:
                result['Backups'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backups = []
        if m.get('Backups') is not None:
            for k in m.get('Backups'):
                temp_model = ListBackupsResponseBodyBackups()
                self.backups.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBackupsResponseBody = None,
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
            temp_model = ListBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        status: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The status of the cluster. Valid values:
        # 
        # *   NEW: The cluster is not initialized.
        # *   INITIALIZED: The cluster is initialized.
        # *   DELETED: The cluster is deleted.
        # *   SYNCHRONIZING: The cluster is being synchronized.
        # *   TO_DELETE: The cluster is pending deletion.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[ListClustersResponseBodyClusters] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The clusters.
        self.clusters = clusters
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of clusters.
        self.total = total

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
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


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        current_page: int = None,
        mode: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the backup.
        # 
        # This parameter is required.
        self.backup_id = backup_id
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The image generation mode. Valid values:
        # 
        # *   PERIODIC: It is automatically generated.
        # *   MANUAL: It is manually generated.
        self.mode = mode
        # The number of images per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        copy_time: str = None,
        export_time: int = None,
        image_id: str = None,
        instance_id: str = None,
        mode: str = None,
        region_id: str = None,
        remark: str = None,
        source_backup_uid: str = None,
        source_image_uid: str = None,
        source_instance_id: str = None,
        source_region_id: str = None,
        status: str = None,
        vsm_digest: str = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id
        # The time when the image was copied. Unit: milliseconds. The value is a UNIX timestamp.
        self.copy_time = copy_time
        # The time when the image was generated. Unit: milliseconds. The value is a UNIX timestamp.
        self.export_time = export_time
        # The ID of the image.
        self.image_id = image_id
        # The ID of the hardware security module (HSM).
        self.instance_id = instance_id
        # The image generation mode. Valid values:
        # 
        # *   PERIODIC: It is automatically generated.
        # *   MANUAL: It is manually generated.
        self.mode = mode
        # The ID of the region.
        self.region_id = region_id
        # The description of the backup.
        self.remark = remark
        # The ID of the source backup.
        self.source_backup_uid = source_backup_uid
        # The ID of the source image.
        self.source_image_uid = source_image_uid
        # The ID of the source HSM.
        self.source_instance_id = source_instance_id
        # The ID of the region in which the source image resides.
        self.source_region_id = source_region_id
        # The status of the image. Valid values:
        # 
        # *   NEW: It is disabled.
        # *   DELETED: It is deleted.
        # *   CREATING: It is being created.
        # *   NORMAL: It is created.
        self.status = status
        # The digest of the HSM.
        self.vsm_digest = vsm_digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.copy_time is not None:
            result['CopyTime'] = self.copy_time
        if self.export_time is not None:
            result['ExportTime'] = self.export_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source_backup_uid is not None:
            result['SourceBackupUid'] = self.source_backup_uid
        if self.source_image_uid is not None:
            result['SourceImageUid'] = self.source_image_uid
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vsm_digest is not None:
            result['VsmDigest'] = self.vsm_digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('CopyTime') is not None:
            self.copy_time = m.get('CopyTime')
        if m.get('ExportTime') is not None:
            self.export_time = m.get('ExportTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SourceBackupUid') is not None:
            self.source_backup_uid = m.get('SourceBackupUid')
        if m.get('SourceImageUid') is not None:
            self.source_image_uid = m.get('SourceImageUid')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VsmDigest') is not None:
            self.vsm_digest = m.get('VsmDigest')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        images: List[ListImagesResponseBodyImages] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The images returned.
        self.images = images
        # The number of images per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of images returned.
        self.total_count = total_count

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
        tenant_isolation_type: str = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of HSMs that is classified based on resource isolation. Valid values:
        # - vsm: Virtual security modules (VSMs).
        # - hostedHsm: Dedicated HSMs.
        self.tenant_isolation_type = tenant_isolation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tenant_isolation_type is not None:
            result['TenantIsolationType'] = self.tenant_isolation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TenantIsolationType') is not None:
            self.tenant_isolation_type = m.get('TenantIsolationType')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
    ):
        # The ID of the HSM.
        self.instance_id = instance_id
        # The HSM status. Valid values:
        # 
        # *   PENDING: The HSM is disabled.
        # *   ACTIVE: The HSM is enabled.
        # *   EXPIRED: The HSM expired.
        # *   INVALID: The HSM is invalid.
        # *   FAILURE: The HSM failed to be created.
        # *   RESET: The HSM is being reset.
        # *   PAUSED: The HSM is paused.
        # *   MODIFYING: The HSM is being modified.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instances: List[ListInstancesResponseBodyInstances] = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The HSMs.
        self.instances = instances
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The ID of the hardware security module (HSM).
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
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


class PauseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class PauseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PauseInstanceResponseBody = None,
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
            temp_model = PauseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuickDeployClusterRequest(TeaModel):
    def __init__(
        self,
        cert_managed: bool = None,
        cluster_name: str = None,
        instance_list: List[str] = None,
        region_id: str = None,
        v_switch_id_list: List[str] = None,
        vpc_id: str = None,
        white_list: List[str] = None,
    ):
        self.cert_managed = cert_managed
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.instance_list = instance_list
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.v_switch_id_list = v_switch_id_list
        # This parameter is required.
        self.vpc_id = vpc_id
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_managed is not None:
            result['CertManaged'] = self.cert_managed
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertManaged') is not None:
            self.cert_managed = m.get('CertManaged')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class QuickDeployClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        cert_managed: bool = None,
        cluster_name: str = None,
        instance_list_shrink: str = None,
        region_id: str = None,
        v_switch_id_list_shrink: str = None,
        vpc_id: str = None,
        white_list_shrink: str = None,
    ):
        self.cert_managed = cert_managed
        # This parameter is required.
        self.cluster_name = cluster_name
        # This parameter is required.
        self.instance_list_shrink = instance_list_shrink
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.v_switch_id_list_shrink = v_switch_id_list_shrink
        # This parameter is required.
        self.vpc_id = vpc_id
        self.white_list_shrink = white_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_managed is not None:
            result['CertManaged'] = self.cert_managed
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_list_shrink is not None:
            result['InstanceList'] = self.instance_list_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id_list_shrink is not None:
            result['VSwitchIdList'] = self.v_switch_id_list_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.white_list_shrink is not None:
            result['WhiteList'] = self.white_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertManaged') is not None:
            self.cert_managed = m.get('CertManaged')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceList') is not None:
            self.instance_list_shrink = m.get('InstanceList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list_shrink = m.get('VSwitchIdList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WhiteList') is not None:
            self.white_list_shrink = m.get('WhiteList')
        return self


class QuickDeployClusterResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.progress = progress
        self.response = response
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QuickDeployClusterResponseBody(TeaModel):
    def __init__(
        self,
        job: QuickDeployClusterResponseBodyJob = None,
        request_id: str = None,
    ):
        self.job = job
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = QuickDeployClusterResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuickDeployClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuickDeployClusterResponseBody = None,
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
            temp_model = QuickDeployClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuickInitInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
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


class QuickInitInstanceResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete.
        self.completed = completed
        # The time when the task is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.create_time = create_time
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The response returned after the task succeeds.
        self.response = response
        # The task status. Valid values:
        # 
        # *   success
        # *   running
        # *   cancel
        # *   fail
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QuickInitInstanceResponseBody(TeaModel):
    def __init__(
        self,
        job: QuickInitInstanceResponseBodyJob = None,
        request_id: str = None,
    ):
        # The details of the task.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = QuickInitInstanceResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuickInitInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuickInitInstanceResponseBody = None,
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
            temp_model = QuickInitInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetBackupRequest(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
    ):
        # The ID of the backup.
        self.backup_id = backup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class ResetBackupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ResetBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetBackupResponseBody = None,
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
            temp_model = ResetBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
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


class ResetInstanceResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete.
        self.completed = completed
        # The time when the task is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.create_time = create_time
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The response returned after the task succeeds.
        self.response = response
        # The task status. Valid values:
        # 
        # *   success
        # *   running
        # *   cancel
        # *   fail
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ResetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        job: ResetInstanceResponseBodyJob = None,
        request_id: str = None,
    ):
        # The details of the task.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = ResetInstanceResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetInstanceResponseBody = None,
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
            temp_model = ResetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreInstanceRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the image that you want to use to restore the HSM.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestoreInstanceResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete.
        self.completed = completed
        # The time when the task is created. The value is accurate to the millisecond. The value is a UNIX timestamp.
        self.create_time = create_time
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The response returned after the task succeeds.
        self.response = response
        # The task status.
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RestoreInstanceResponseBody(TeaModel):
    def __init__(
        self,
        job: RestoreInstanceResponseBodyJob = None,
        request_id: str = None,
    ):
        # The details of the task.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = RestoreInstanceResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestoreInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestoreInstanceResponseBody = None,
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
            temp_model = RestoreInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the HSM.
        # 
        # This parameter is required.
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


class ResumeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ResumeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeInstanceResponseBody = None,
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
            temp_model = ResumeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RotateClusterManagedCertRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class RotateClusterManagedCertResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        process: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.process = process
        self.response = response
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.process is not None:
            result['Process'] = self.process
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RotateClusterManagedCertResponseBody(TeaModel):
    def __init__(
        self,
        job: RotateClusterManagedCertResponseBodyJob = None,
        request_id: str = None,
    ):
        self.job = job
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = RotateClusterManagedCertResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RotateClusterManagedCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RotateClusterManagedCertResponseBody = None,
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
            temp_model = RotateClusterManagedCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchClusterMasterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the HSM that you want to promote to the master HSM.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SwitchClusterMasterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class SwitchClusterMasterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchClusterMasterResponseBody = None,
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
            temp_model = SwitchClusterMasterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class SyncClusterResponseBodyJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        # Indicates whether the task is complete. Valid values:
        # 
        # *   true
        # *   false
        self.completed = completed
        # The time when the task was created. Unit: milliseconds. The value is a UNIX timestamp.
        self.create_time = create_time
        # The error message returned if the task fails.
        self.error = error
        # The ID of the task.
        self.job_id = job_id
        # The progress of the task. Unit: percent (%).
        self.progress = progress
        # The response returned after the task succeeds.
        self.response = response
        # The status of the task. Valid values:
        # 
        # *   success
        # *   running
        # *   cancel
        # *   fail
        self.status = status
        # The operation type. Valid values:
        # 
        # *   create
        # *   cancel
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SyncClusterResponseBody(TeaModel):
    def __init__(
        self,
        job: SyncClusterResponseBodyJob = None,
        request_id: str = None,
    ):
        # The details of the task.
        self.job = job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = SyncClusterResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncClusterResponseBody = None,
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
            temp_model = SyncClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


