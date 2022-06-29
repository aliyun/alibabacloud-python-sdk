# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CloneFlowJobRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # 克隆的目标作业ID。您可以调用ListFlowJob查看。
        self.id = id
        # 克隆的目标作业名称。
        self.name = name
        # 克隆的目标作业所属项目。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CloneFlowJobResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # 新产生的作业ID。
        self.id = id
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CloneFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterV2RequestBootstrapAction(TeaModel):
    def __init__(
        self,
        arg: str = None,
        name: str = None,
        path: str = None,
    ):
        self.arg = arg
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateClusterV2RequestConfig(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        config_value: str = None,
        encrypt: str = None,
        file_name: str = None,
        replace: str = None,
        service_name: str = None,
    ):
        self.config_key = config_key
        self.config_value = config_value
        self.encrypt = encrypt
        self.file_name = file_name
        self.replace = replace
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateClusterV2RequestHostComponentInfo(TeaModel):
    def __init__(
        self,
        component_name_list: List[str] = None,
        host_name: str = None,
        service_name: str = None,
    ):
        self.component_name_list = component_name_list
        self.host_name = host_name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name_list is not None:
            result['ComponentNameList'] = self.component_name_list
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentNameList') is not None:
            self.component_name_list = m.get('ComponentNameList')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CreateClusterV2RequestHostGroup(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        charge_type: str = None,
        cluster_id: str = None,
        comment: str = None,
        create_type: str = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        gpu_driver: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
        host_group_type: str = None,
        instance_type: str = None,
        node_count: int = None,
        period: int = None,
        sys_disk_capacity: int = None,
        sys_disk_type: str = None,
        v_switch_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.cluster_id = cluster_id
        self.comment = comment
        self.create_type = create_type
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.gpu_driver = gpu_driver
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name
        self.host_group_type = host_group_type
        self.instance_type = instance_type
        self.node_count = node_count
        self.period = period
        self.sys_disk_capacity = sys_disk_capacity
        self.sys_disk_type = sys_disk_type
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.gpu_driver is not None:
            result['GpuDriver'] = self.gpu_driver
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.period is not None:
            result['Period'] = self.period
        if self.sys_disk_capacity is not None:
            result['SysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_type is not None:
            result['SysDiskType'] = self.sys_disk_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('GpuDriver') is not None:
            self.gpu_driver = m.get('GpuDriver')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('SysDiskCapacity')
        if m.get('SysDiskType') is not None:
            self.sys_disk_type = m.get('SysDiskType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateClusterV2RequestPromotionInfo(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        self.product_code = product_code
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code
        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')
        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')
        return self


class CreateClusterV2RequestServiceInfo(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        service_version: str = None,
    ):
        self.service_name = service_name
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class CreateClusterV2RequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateClusterV2RequestUserInfo(TeaModel):
    def __init__(
        self,
        password: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.password = password
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateClusterV2Request(TeaModel):
    def __init__(
        self,
        authorize_content: str = None,
        auto: bool = None,
        auto_pay_order: bool = None,
        bootstrap_action: List[CreateClusterV2RequestBootstrapAction] = None,
        charge_type: str = None,
        click_house_conf: str = None,
        client_token: str = None,
        cluster_type: str = None,
        config: List[CreateClusterV2RequestConfig] = None,
        configurations: str = None,
        deposit_type: str = None,
        emr_ver: str = None,
        enable_eas: bool = None,
        enable_high_availability: bool = None,
        enable_ssh: bool = None,
        extra_attributes: str = None,
        host_component_info: List[CreateClusterV2RequestHostComponentInfo] = None,
        host_group: List[CreateClusterV2RequestHostGroup] = None,
        init_custom_hive_meta_db: bool = None,
        instance_generation: str = None,
        is_open_public_ip: bool = None,
        key_pair_name: str = None,
        log_path: str = None,
        machine_type: str = None,
        master_pwd: str = None,
        meta_store_conf: str = None,
        meta_store_type: str = None,
        name: str = None,
        net_type: str = None,
        period: int = None,
        promotion_info: List[CreateClusterV2RequestPromotionInfo] = None,
        region_id: str = None,
        related_cluster_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        security_group_name: str = None,
        service_info: List[CreateClusterV2RequestServiceInfo] = None,
        tag: List[CreateClusterV2RequestTag] = None,
        use_custom_hive_meta_db: bool = None,
        use_local_meta_db: bool = None,
        user_defined_emr_ecs_role: str = None,
        user_info: List[CreateClusterV2RequestUserInfo] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        white_list_type: str = None,
        zone_id: str = None,
    ):
        self.authorize_content = authorize_content
        self.auto = auto
        self.auto_pay_order = auto_pay_order
        self.bootstrap_action = bootstrap_action
        self.charge_type = charge_type
        self.click_house_conf = click_house_conf
        self.client_token = client_token
        self.cluster_type = cluster_type
        self.config = config
        self.configurations = configurations
        self.deposit_type = deposit_type
        self.emr_ver = emr_ver
        self.enable_eas = enable_eas
        self.enable_high_availability = enable_high_availability
        self.enable_ssh = enable_ssh
        self.extra_attributes = extra_attributes
        self.host_component_info = host_component_info
        self.host_group = host_group
        self.init_custom_hive_meta_db = init_custom_hive_meta_db
        self.instance_generation = instance_generation
        self.is_open_public_ip = is_open_public_ip
        self.key_pair_name = key_pair_name
        self.log_path = log_path
        self.machine_type = machine_type
        self.master_pwd = master_pwd
        self.meta_store_conf = meta_store_conf
        self.meta_store_type = meta_store_type
        self.name = name
        self.net_type = net_type
        self.period = period
        self.promotion_info = promotion_info
        self.region_id = region_id
        self.related_cluster_id = related_cluster_id
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.service_info = service_info
        self.tag = tag
        self.use_custom_hive_meta_db = use_custom_hive_meta_db
        self.use_local_meta_db = use_local_meta_db
        self.user_defined_emr_ecs_role = user_defined_emr_ecs_role
        self.user_info = user_info
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.white_list_type = white_list_type
        self.zone_id = zone_id

    def validate(self):
        if self.bootstrap_action:
            for k in self.bootstrap_action:
                if k:
                    k.validate()
        if self.config:
            for k in self.config:
                if k:
                    k.validate()
        if self.host_component_info:
            for k in self.host_component_info:
                if k:
                    k.validate()
        if self.host_group:
            for k in self.host_group:
                if k:
                    k.validate()
        if self.promotion_info:
            for k in self.promotion_info:
                if k:
                    k.validate()
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.user_info:
            for k in self.user_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_content is not None:
            result['AuthorizeContent'] = self.authorize_content
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.auto_pay_order is not None:
            result['AutoPayOrder'] = self.auto_pay_order
        result['BootstrapAction'] = []
        if self.bootstrap_action is not None:
            for k in self.bootstrap_action:
                result['BootstrapAction'].append(k.to_map() if k else None)
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.click_house_conf is not None:
            result['ClickHouseConf'] = self.click_house_conf
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        if self.configurations is not None:
            result['Configurations'] = self.configurations
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.emr_ver is not None:
            result['EmrVer'] = self.emr_ver
        if self.enable_eas is not None:
            result['EnableEas'] = self.enable_eas
        if self.enable_high_availability is not None:
            result['EnableHighAvailability'] = self.enable_high_availability
        if self.enable_ssh is not None:
            result['EnableSsh'] = self.enable_ssh
        if self.extra_attributes is not None:
            result['ExtraAttributes'] = self.extra_attributes
        result['HostComponentInfo'] = []
        if self.host_component_info is not None:
            for k in self.host_component_info:
                result['HostComponentInfo'].append(k.to_map() if k else None)
        result['HostGroup'] = []
        if self.host_group is not None:
            for k in self.host_group:
                result['HostGroup'].append(k.to_map() if k else None)
        if self.init_custom_hive_meta_db is not None:
            result['InitCustomHiveMetaDB'] = self.init_custom_hive_meta_db
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.is_open_public_ip is not None:
            result['IsOpenPublicIp'] = self.is_open_public_ip
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.master_pwd is not None:
            result['MasterPwd'] = self.master_pwd
        if self.meta_store_conf is not None:
            result['MetaStoreConf'] = self.meta_store_conf
        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type
        if self.name is not None:
            result['Name'] = self.name
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.period is not None:
            result['Period'] = self.period
        result['PromotionInfo'] = []
        if self.promotion_info is not None:
            for k in self.promotion_info:
                result['PromotionInfo'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.related_cluster_id is not None:
            result['RelatedClusterId'] = self.related_cluster_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.use_custom_hive_meta_db is not None:
            result['UseCustomHiveMetaDB'] = self.use_custom_hive_meta_db
        if self.use_local_meta_db is not None:
            result['UseLocalMetaDb'] = self.use_local_meta_db
        if self.user_defined_emr_ecs_role is not None:
            result['UserDefinedEmrEcsRole'] = self.user_defined_emr_ecs_role
        result['UserInfo'] = []
        if self.user_info is not None:
            for k in self.user_info:
                result['UserInfo'].append(k.to_map() if k else None)
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeContent') is not None:
            self.authorize_content = m.get('AuthorizeContent')
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('AutoPayOrder') is not None:
            self.auto_pay_order = m.get('AutoPayOrder')
        self.bootstrap_action = []
        if m.get('BootstrapAction') is not None:
            for k in m.get('BootstrapAction'):
                temp_model = CreateClusterV2RequestBootstrapAction()
                self.bootstrap_action.append(temp_model.from_map(k))
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClickHouseConf') is not None:
            self.click_house_conf = m.get('ClickHouseConf')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = CreateClusterV2RequestConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('Configurations') is not None:
            self.configurations = m.get('Configurations')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('EmrVer') is not None:
            self.emr_ver = m.get('EmrVer')
        if m.get('EnableEas') is not None:
            self.enable_eas = m.get('EnableEas')
        if m.get('EnableHighAvailability') is not None:
            self.enable_high_availability = m.get('EnableHighAvailability')
        if m.get('EnableSsh') is not None:
            self.enable_ssh = m.get('EnableSsh')
        if m.get('ExtraAttributes') is not None:
            self.extra_attributes = m.get('ExtraAttributes')
        self.host_component_info = []
        if m.get('HostComponentInfo') is not None:
            for k in m.get('HostComponentInfo'):
                temp_model = CreateClusterV2RequestHostComponentInfo()
                self.host_component_info.append(temp_model.from_map(k))
        self.host_group = []
        if m.get('HostGroup') is not None:
            for k in m.get('HostGroup'):
                temp_model = CreateClusterV2RequestHostGroup()
                self.host_group.append(temp_model.from_map(k))
        if m.get('InitCustomHiveMetaDB') is not None:
            self.init_custom_hive_meta_db = m.get('InitCustomHiveMetaDB')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('IsOpenPublicIp') is not None:
            self.is_open_public_ip = m.get('IsOpenPublicIp')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MasterPwd') is not None:
            self.master_pwd = m.get('MasterPwd')
        if m.get('MetaStoreConf') is not None:
            self.meta_store_conf = m.get('MetaStoreConf')
        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.promotion_info = []
        if m.get('PromotionInfo') is not None:
            for k in m.get('PromotionInfo'):
                temp_model = CreateClusterV2RequestPromotionInfo()
                self.promotion_info.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelatedClusterId') is not None:
            self.related_cluster_id = m.get('RelatedClusterId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = CreateClusterV2RequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterV2RequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UseCustomHiveMetaDB') is not None:
            self.use_custom_hive_meta_db = m.get('UseCustomHiveMetaDB')
        if m.get('UseLocalMetaDb') is not None:
            self.use_local_meta_db = m.get('UseLocalMetaDb')
        if m.get('UserDefinedEmrEcsRole') is not None:
            self.user_defined_emr_ecs_role = m.get('UserDefinedEmrEcsRole')
        self.user_info = []
        if m.get('UserInfo') is not None:
            for k in m.get('UserInfo'):
                temp_model = CreateClusterV2RequestUserInfo()
                self.user_info.append(temp_model.from_map(k))
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterV2ResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        core_order_id: str = None,
        emr_order_id: str = None,
        master_order_id: str = None,
        request_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.core_order_id = core_order_id
        self.emr_order_id = emr_order_id
        self.master_order_id = master_order_id
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
        if self.core_order_id is not None:
            result['CoreOrderId'] = self.core_order_id
        if self.emr_order_id is not None:
            result['EmrOrderId'] = self.emr_order_id
        if self.master_order_id is not None:
            result['MasterOrderId'] = self.master_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreOrderId') is not None:
            self.core_order_id = m.get('CoreOrderId')
        if m.get('EmrOrderId') is not None:
            self.emr_order_id = m.get('EmrOrderId')
        if m.get('MasterOrderId') is not None:
            self.master_order_id = m.get('MasterOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateClusterV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        alert_conf: str = None,
        alert_ding_ding_group_biz_id: str = None,
        alert_user_group_biz_id: str = None,
        application: str = None,
        client_token: str = None,
        cluster_id: str = None,
        create_cluster: bool = None,
        cron_expression: str = None,
        description: str = None,
        end_schedule: int = None,
        host_name: str = None,
        name: str = None,
        namespace: str = None,
        parent_category: str = None,
        parent_flow_list: str = None,
        project_id: str = None,
        region_id: str = None,
        start_schedule: int = None,
    ):
        self.alert_conf = alert_conf
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id
        self.alert_user_group_biz_id = alert_user_group_biz_id
        self.application = application
        self.client_token = client_token
        self.cluster_id = cluster_id
        self.create_cluster = create_cluster
        self.cron_expression = cron_expression
        self.description = description
        self.end_schedule = end_schedule
        self.host_name = host_name
        self.name = name
        self.namespace = namespace
        self.parent_category = parent_category
        self.parent_flow_list = parent_flow_list
        self.project_id = project_id
        self.region_id = region_id
        self.start_schedule = start_schedule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.application is not None:
            result['Application'] = self.application
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ParentFlowList') is not None:
            self.parent_flow_list = m.get('ParentFlowList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowCategoryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        name: str = None,
        parent_id: str = None,
        project_id: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.client_token = client_token
        self.name = name
        self.parent_id = parent_id
        self.project_id = project_id
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowCategoryResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFlowCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowJobRequestResourceList(TeaModel):
    def __init__(
        self,
        alias: str = None,
        path: str = None,
    ):
        # 保留参数。
        self.alias = alias
        # 保留参数。
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class CreateFlowJobRequest(TeaModel):
    def __init__(
        self,
        adhoc: bool = None,
        alert_conf: str = None,
        client_token: str = None,
        cluster_id: str = None,
        custom_variables: str = None,
        description: str = None,
        env_conf: str = None,
        fail_act: str = None,
        mode: str = None,
        monitor_conf: str = None,
        name: str = None,
        param_conf: str = None,
        params: str = None,
        parent_category: str = None,
        project_id: str = None,
        region_id: str = None,
        resource_list: List[CreateFlowJobRequestResourceList] = None,
        retry_policy: str = None,
        run_conf: str = None,
        type: str = None,
    ):
        # 是否临时查询。
        self.adhoc = adhoc
        # 保留参数。
        self.alert_conf = alert_conf
        # 保留参数。
        self.client_token = client_token
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id
        # 自定义变量。
        self.custom_variables = custom_variables
        # 作业的描述。
        self.description = description
        # 环境变量设置。
        self.env_conf = env_conf
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf
        # 作业的名称。
        self.name = name
        # 参数设置。
        self.param_conf = param_conf
        # 作业内容。
        self.params = params
        # 父目录ID。您可以调用DescribeFlowCategory查看。
        self.parent_category = parent_category
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id
        # 保留参数。
        self.resource_list = resource_list
        # 重试策略，保留参数。
        self.retry_policy = retry_policy
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
        self.type = type

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = CreateFlowJobRequestResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowJobResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # 作业ID。
        self.id = id
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        product_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.client_token = client_token
        # 项目描述
        self.description = description
        # 项目名称
        self.name = name
        # 产品类型，固定值DATABRICKS_DATAINSIGHT
        self.product_type = product_type
        # 地域ID
        self.region_id = region_id
        # 资源组ID
        self.resource_group_id = resource_group_id

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
        if self.name is not None:
            result['Name'] = self.name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateFlowProjectResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # 项目ID
        self.id = id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowProjectUserRequestUser(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateFlowProjectUserRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: str = None,
        region_id: str = None,
        user: List[CreateFlowProjectUserRequestUser] = None,
    ):
        self.client_token = client_token
        self.project_id = project_id
        self.region_id = region_id
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = CreateFlowProjectUserRequestUser()
                self.user.append(temp_model.from_map(k))
        return self


class CreateFlowProjectUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowProjectUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowProjectUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLibraryRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        library_version: str = None,
        name: str = None,
        properties: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        scope: str = None,
        source_location: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.client_token = client_token
        self.library_version = library_version
        self.name = name
        self.properties = properties
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.scope = scope
        self.source_location = source_location
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.library_version is not None:
            result['LibraryVersion'] = self.library_version
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LibraryVersion') is not None:
            self.library_version = m.get('LibraryVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateLibraryResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLibraryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLibraryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateLibraryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowCategoryRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowCategoryResponseBody(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        job_id: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.flow_id = flow_id
        self.job_id = job_id
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteFlowCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteFlowCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        region_id: str = None,
    ):
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteFlowProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowProjectUserRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        region_id: str = None,
        user_name: str = None,
    ):
        self.project_id = project_id
        self.region_id = region_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteFlowProjectUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowProjectUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowProjectUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLibrariesRequest(TeaModel):
    def __init__(
        self,
        library_biz_id_list: List[str] = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.library_biz_id_list = library_biz_id_list
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_biz_id_list is not None:
            result['LibraryBizIdList'] = self.library_biz_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibraryBizIdList') is not None:
            self.library_biz_id_list = m.get('LibraryBizIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteLibrariesResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLibrariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLibrariesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterV2Request(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.id = id
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink(TeaModel):
    def __init__(
        self,
        link: str = None,
        port: str = None,
    ):
        self.link = link
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link is not None:
            result['Link'] = self.link
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks(TeaModel):
    def __init__(
        self,
        zklink: List[DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink] = None,
    ):
        self.zklink = zklink

    def validate(self):
        if self.zklink:
            for k in self.zklink:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZKLink'] = []
        if self.zklink is not None:
            for k in self.zklink:
                result['ZKLink'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zklink = []
        if m.get('ZKLink') is not None:
            for k in m.get('ZKLink'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinksZKLink()
                self.zklink.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoAccessInfo(TeaModel):
    def __init__(
        self,
        zklinks: DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks = None,
    ):
        self.zklinks = zklinks

    def validate(self):
        if self.zklinks:
            self.zklinks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zklinks is not None:
            result['ZKLinks'] = self.zklinks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZKLinks') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoAccessInfoZKLinks()
            self.zklinks = temp_model.from_map(m['ZKLinks'])
        return self


class DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction(TeaModel):
    def __init__(
        self,
        arg: str = None,
        name: str = None,
        path: str = None,
    ):
        self.arg = arg
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg is not None:
            result['Arg'] = self.arg
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList(TeaModel):
    def __init__(
        self,
        bootstrap_action: List[DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction] = None,
    ):
        self.bootstrap_action = bootstrap_action

    def validate(self):
        if self.bootstrap_action:
            for k in self.bootstrap_action:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BootstrapAction'] = []
        if self.bootstrap_action is not None:
            for k in self.bootstrap_action:
                result['BootstrapAction'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bootstrap_action = []
        if m.get('BootstrapAction') is not None:
            for k in m.get('BootstrapAction'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoBootstrapActionListBootstrapAction()
                self.bootstrap_action.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoFailReason(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
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
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList(TeaModel):
    def __init__(
        self,
        gateway_cluster_info: List[DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo] = None,
    ):
        self.gateway_cluster_info = gateway_cluster_info

    def validate(self):
        if self.gateway_cluster_info:
            for k in self.gateway_cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewayClusterInfo'] = []
        if self.gateway_cluster_info is not None:
            for k in self.gateway_cluster_info:
                result['GatewayClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_cluster_info = []
        if m.get('GatewayClusterInfo') is not None:
            for k in m.get('GatewayClusterInfo'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoListGatewayClusterInfo()
                self.gateway_cluster_info.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos(TeaModel):
    def __init__(
        self,
        daemon_info: List[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo] = None,
    ):
        self.daemon_info = daemon_info

    def validate(self):
        if self.daemon_info:
            for k in self.daemon_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DaemonInfo'] = []
        if self.daemon_info is not None:
            for k in self.daemon_info:
                result['DaemonInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daemon_info = []
        if m.get('DaemonInfo') is not None:
            for k in m.get('DaemonInfo'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfosDaemonInfo()
                self.daemon_info.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo(TeaModel):
    def __init__(
        self,
        device: str = None,
        disk_id: str = None,
        disk_name: str = None,
        size: int = None,
        type: str = None,
    ):
        self.device = device
        self.disk_id = disk_id
        self.disk_name = disk_name
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos(TeaModel):
    def __init__(
        self,
        disk_info: List[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo] = None,
    ):
        self.disk_info = disk_info

    def validate(self):
        if self.disk_info:
            for k in self.disk_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiskInfo'] = []
        if self.disk_info is not None:
            for k in self.disk_info:
                result['DiskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_info = []
        if m.get('DiskInfo') is not None:
            for k in m.get('DiskInfo'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfosDiskInfo()
                self.disk_info.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        daemon_infos: DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos = None,
        disk_infos: DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos = None,
        emr_expired_time: str = None,
        expired_time: str = None,
        inner_ip: str = None,
        instance_id: str = None,
        pub_ip: str = None,
        status: str = None,
        support_ip_v6: bool = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.daemon_infos = daemon_infos
        self.disk_infos = disk_infos
        self.emr_expired_time = emr_expired_time
        self.expired_time = expired_time
        self.inner_ip = inner_ip
        self.instance_id = instance_id
        self.pub_ip = pub_ip
        self.status = status
        self.support_ip_v6 = support_ip_v6
        self.zone_id = zone_id

    def validate(self):
        if self.daemon_infos:
            self.daemon_infos.validate()
        if self.disk_infos:
            self.disk_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.daemon_infos is not None:
            result['DaemonInfos'] = self.daemon_infos.to_map()
        if self.disk_infos is not None:
            result['DiskInfos'] = self.disk_infos.to_map()
        if self.emr_expired_time is not None:
            result['EmrExpiredTime'] = self.emr_expired_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.inner_ip is not None:
            result['InnerIp'] = self.inner_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pub_ip is not None:
            result['PubIp'] = self.pub_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.support_ip_v6 is not None:
            result['SupportIpV6'] = self.support_ip_v6
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DaemonInfos') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDaemonInfos()
            self.daemon_infos = temp_model.from_map(m['DaemonInfos'])
        if m.get('DiskInfos') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNodeDiskInfos()
            self.disk_infos = temp_model.from_map(m['DiskInfos'])
        if m.get('EmrExpiredTime') is not None:
            self.emr_expired_time = m.get('EmrExpiredTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InnerIp') is not None:
            self.inner_ip = m.get('InnerIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PubIp') is not None:
            self.pub_ip = m.get('PubIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportIpV6') is not None:
            self.support_ip_v6 = m.get('SupportIpV6')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes(TeaModel):
    def __init__(
        self,
        node: List[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodesNode()
                self.node.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup(TeaModel):
    def __init__(
        self,
        band_width: str = None,
        charge_type: str = None,
        cpu_core: int = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        host_group_change_status: str = None,
        host_group_change_type: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
        host_group_sub_type: str = None,
        host_group_type: str = None,
        instance_type: str = None,
        lock_reason: str = None,
        lock_type: str = None,
        memory_capacity: int = None,
        node_count: int = None,
        nodes: DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes = None,
        period: str = None,
    ):
        self.band_width = band_width
        self.charge_type = charge_type
        self.cpu_core = cpu_core
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.host_group_change_status = host_group_change_status
        self.host_group_change_type = host_group_change_type
        self.host_group_id = host_group_id
        self.host_group_name = host_group_name
        self.host_group_sub_type = host_group_sub_type
        self.host_group_type = host_group_type
        self.instance_type = instance_type
        self.lock_reason = lock_reason
        self.lock_type = lock_type
        self.memory_capacity = memory_capacity
        self.node_count = node_count
        self.nodes = nodes
        self.period = period

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_core is not None:
            result['CpuCore'] = self.cpu_core
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_change_status is not None:
            result['HostGroupChangeStatus'] = self.host_group_change_status
        if self.host_group_change_type is not None:
            result['HostGroupChangeType'] = self.host_group_change_type
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_sub_type is not None:
            result['HostGroupSubType'] = self.host_group_sub_type
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        if self.memory_capacity is not None:
            result['MemoryCapacity'] = self.memory_capacity
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuCore') is not None:
            self.cpu_core = m.get('CpuCore')
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupChangeStatus') is not None:
            self.host_group_change_status = m.get('HostGroupChangeStatus')
        if m.get('HostGroupChangeType') is not None:
            self.host_group_change_type = m.get('HostGroupChangeType')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupSubType') is not None:
            self.host_group_sub_type = m.get('HostGroupSubType')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        if m.get('MemoryCapacity') is not None:
            self.memory_capacity = m.get('MemoryCapacity')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Nodes') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroupNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostGroupList(TeaModel):
    def __init__(
        self,
        host_group: List[DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup] = None,
    ):
        self.host_group = host_group

    def validate(self):
        if self.host_group:
            for k in self.host_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroup'] = []
        if self.host_group is not None:
            for k in self.host_group:
                result['HostGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_group = []
        if m.get('HostGroup') is not None:
            for k in m.get('HostGroup'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupListHostGroup()
                self.host_group.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo(TeaModel):
    def __init__(
        self,
        hp_biz_id: str = None,
        hp_name: str = None,
    ):
        self.hp_biz_id = hp_biz_id
        self.hp_name = hp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hp_biz_id is not None:
            result['HpBizId'] = self.hp_biz_id
        if self.hp_name is not None:
            result['HpName'] = self.hp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HpBizId') is not None:
            self.hp_biz_id = m.get('HpBizId')
        if m.get('HpName') is not None:
            self.hp_name = m.get('HpName')
        return self


class DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
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
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        only_display: bool = None,
        start_tpe: int = None,
        version: str = None,
    ):
        self.display_name = display_name
        self.name = name
        self.only_display = only_display
        self.start_tpe = start_tpe
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.only_display is not None:
            result['OnlyDisplay'] = self.only_display
        if self.start_tpe is not None:
            result['StartTpe'] = self.start_tpe
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OnlyDisplay') is not None:
            self.only_display = m.get('OnlyDisplay')
        if m.get('StartTpe') is not None:
            self.start_tpe = m.get('StartTpe')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares(TeaModel):
    def __init__(
        self,
        software: List[DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware] = None,
    ):
        self.software = software

    def validate(self):
        if self.software:
            for k in self.software:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Software'] = []
        if self.software is not None:
            for k in self.software:
                result['Software'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.software = []
        if m.get('Software') is not None:
            for k in m.get('Software'):
                temp_model = DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwaresSoftware()
                self.software.append(temp_model.from_map(k))
        return self


class DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        emr_ver: str = None,
        softwares: DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares = None,
    ):
        self.cluster_type = cluster_type
        self.emr_ver = emr_ver
        self.softwares = softwares

    def validate(self):
        if self.softwares:
            self.softwares.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.emr_ver is not None:
            result['EmrVer'] = self.emr_ver
        if self.softwares is not None:
            result['Softwares'] = self.softwares.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('EmrVer') is not None:
            self.emr_ver = m.get('EmrVer')
        if m.get('Softwares') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoSoftwareInfoSoftwares()
            self.softwares = temp_model.from_map(m['Softwares'])
        return self


class DescribeClusterV2ResponseBodyClusterInfo(TeaModel):
    def __init__(
        self,
        access_info: DescribeClusterV2ResponseBodyClusterInfoAccessInfo = None,
        auto_scaling_allowed: bool = None,
        auto_scaling_by_load_allowed: bool = None,
        auto_scaling_enable: bool = None,
        auto_scaling_spot_with_limit_allowed: bool = None,
        auto_scaling_version: str = None,
        auto_scaling_with_grace_allowed: bool = None,
        bootstrap_action_list: DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList = None,
        bootstrap_failed: bool = None,
        charge_type: str = None,
        configurations: str = None,
        core_node_in_service: int = None,
        core_node_total: int = None,
        create_resource: str = None,
        create_type: str = None,
        deposit_type: str = None,
        eas_enable: bool = None,
        expired_time: int = None,
        extra_info: str = None,
        fail_reason: DescribeClusterV2ResponseBodyClusterInfoFailReason = None,
        gateway_cluster_ids: str = None,
        gateway_cluster_info_list: DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList = None,
        high_availability_enable: bool = None,
        host_group_list: DescribeClusterV2ResponseBodyClusterInfoHostGroupList = None,
        host_pool_info: DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo = None,
        id: str = None,
        image_id: str = None,
        instance_generation: str = None,
        io_optimized: bool = None,
        k_8s_cluster_id: str = None,
        local_meta_db: bool = None,
        log_enable: bool = None,
        log_path: str = None,
        machine_type: str = None,
        master_node_in_service: int = None,
        master_node_total: int = None,
        meta_store_type: str = None,
        name: str = None,
        net_type: str = None,
        period: int = None,
        region_id: str = None,
        relate_cluster_id: str = None,
        relate_cluster_info: DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo = None,
        resize_disk_enable: bool = None,
        running_time: int = None,
        security_group_id: str = None,
        security_group_name: str = None,
        show_software_interface: bool = None,
        software_info: DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo = None,
        start_time: int = None,
        status: str = None,
        stop_time: int = None,
        task_node_in_service: int = None,
        task_node_total: int = None,
        user_defined_emr_ecs_role: str = None,
        user_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.access_info = access_info
        self.auto_scaling_allowed = auto_scaling_allowed
        self.auto_scaling_by_load_allowed = auto_scaling_by_load_allowed
        self.auto_scaling_enable = auto_scaling_enable
        self.auto_scaling_spot_with_limit_allowed = auto_scaling_spot_with_limit_allowed
        self.auto_scaling_version = auto_scaling_version
        self.auto_scaling_with_grace_allowed = auto_scaling_with_grace_allowed
        self.bootstrap_action_list = bootstrap_action_list
        self.bootstrap_failed = bootstrap_failed
        self.charge_type = charge_type
        self.configurations = configurations
        self.core_node_in_service = core_node_in_service
        self.core_node_total = core_node_total
        self.create_resource = create_resource
        self.create_type = create_type
        self.deposit_type = deposit_type
        self.eas_enable = eas_enable
        self.expired_time = expired_time
        self.extra_info = extra_info
        self.fail_reason = fail_reason
        self.gateway_cluster_ids = gateway_cluster_ids
        self.gateway_cluster_info_list = gateway_cluster_info_list
        self.high_availability_enable = high_availability_enable
        self.host_group_list = host_group_list
        self.host_pool_info = host_pool_info
        self.id = id
        self.image_id = image_id
        self.instance_generation = instance_generation
        self.io_optimized = io_optimized
        self.k_8s_cluster_id = k_8s_cluster_id
        self.local_meta_db = local_meta_db
        self.log_enable = log_enable
        self.log_path = log_path
        self.machine_type = machine_type
        self.master_node_in_service = master_node_in_service
        self.master_node_total = master_node_total
        self.meta_store_type = meta_store_type
        self.name = name
        self.net_type = net_type
        self.period = period
        self.region_id = region_id
        self.relate_cluster_id = relate_cluster_id
        self.relate_cluster_info = relate_cluster_info
        self.resize_disk_enable = resize_disk_enable
        self.running_time = running_time
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.show_software_interface = show_software_interface
        self.software_info = software_info
        self.start_time = start_time
        self.status = status
        self.stop_time = stop_time
        self.task_node_in_service = task_node_in_service
        self.task_node_total = task_node_total
        self.user_defined_emr_ecs_role = user_defined_emr_ecs_role
        self.user_id = user_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.access_info:
            self.access_info.validate()
        if self.bootstrap_action_list:
            self.bootstrap_action_list.validate()
        if self.fail_reason:
            self.fail_reason.validate()
        if self.gateway_cluster_info_list:
            self.gateway_cluster_info_list.validate()
        if self.host_group_list:
            self.host_group_list.validate()
        if self.host_pool_info:
            self.host_pool_info.validate()
        if self.relate_cluster_info:
            self.relate_cluster_info.validate()
        if self.software_info:
            self.software_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_info is not None:
            result['AccessInfo'] = self.access_info.to_map()
        if self.auto_scaling_allowed is not None:
            result['AutoScalingAllowed'] = self.auto_scaling_allowed
        if self.auto_scaling_by_load_allowed is not None:
            result['AutoScalingByLoadAllowed'] = self.auto_scaling_by_load_allowed
        if self.auto_scaling_enable is not None:
            result['AutoScalingEnable'] = self.auto_scaling_enable
        if self.auto_scaling_spot_with_limit_allowed is not None:
            result['AutoScalingSpotWithLimitAllowed'] = self.auto_scaling_spot_with_limit_allowed
        if self.auto_scaling_version is not None:
            result['AutoScalingVersion'] = self.auto_scaling_version
        if self.auto_scaling_with_grace_allowed is not None:
            result['AutoScalingWithGraceAllowed'] = self.auto_scaling_with_grace_allowed
        if self.bootstrap_action_list is not None:
            result['BootstrapActionList'] = self.bootstrap_action_list.to_map()
        if self.bootstrap_failed is not None:
            result['BootstrapFailed'] = self.bootstrap_failed
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.configurations is not None:
            result['Configurations'] = self.configurations
        if self.core_node_in_service is not None:
            result['CoreNodeInService'] = self.core_node_in_service
        if self.core_node_total is not None:
            result['CoreNodeTotal'] = self.core_node_total
        if self.create_resource is not None:
            result['CreateResource'] = self.create_resource
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.eas_enable is not None:
            result['EasEnable'] = self.eas_enable
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason.to_map()
        if self.gateway_cluster_ids is not None:
            result['GatewayClusterIds'] = self.gateway_cluster_ids
        if self.gateway_cluster_info_list is not None:
            result['GatewayClusterInfoList'] = self.gateway_cluster_info_list.to_map()
        if self.high_availability_enable is not None:
            result['HighAvailabilityEnable'] = self.high_availability_enable
        if self.host_group_list is not None:
            result['HostGroupList'] = self.host_group_list.to_map()
        if self.host_pool_info is not None:
            result['HostPoolInfo'] = self.host_pool_info.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.local_meta_db is not None:
            result['LocalMetaDb'] = self.local_meta_db
        if self.log_enable is not None:
            result['LogEnable'] = self.log_enable
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.master_node_in_service is not None:
            result['MasterNodeInService'] = self.master_node_in_service
        if self.master_node_total is not None:
            result['MasterNodeTotal'] = self.master_node_total
        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type
        if self.name is not None:
            result['Name'] = self.name
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.relate_cluster_id is not None:
            result['RelateClusterId'] = self.relate_cluster_id
        if self.relate_cluster_info is not None:
            result['RelateClusterInfo'] = self.relate_cluster_info.to_map()
        if self.resize_disk_enable is not None:
            result['ResizeDiskEnable'] = self.resize_disk_enable
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.show_software_interface is not None:
            result['ShowSoftwareInterface'] = self.show_software_interface
        if self.software_info is not None:
            result['SoftwareInfo'] = self.software_info.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.task_node_in_service is not None:
            result['TaskNodeInService'] = self.task_node_in_service
        if self.task_node_total is not None:
            result['TaskNodeTotal'] = self.task_node_total
        if self.user_defined_emr_ecs_role is not None:
            result['UserDefinedEmrEcsRole'] = self.user_defined_emr_ecs_role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoAccessInfo()
            self.access_info = temp_model.from_map(m['AccessInfo'])
        if m.get('AutoScalingAllowed') is not None:
            self.auto_scaling_allowed = m.get('AutoScalingAllowed')
        if m.get('AutoScalingByLoadAllowed') is not None:
            self.auto_scaling_by_load_allowed = m.get('AutoScalingByLoadAllowed')
        if m.get('AutoScalingEnable') is not None:
            self.auto_scaling_enable = m.get('AutoScalingEnable')
        if m.get('AutoScalingSpotWithLimitAllowed') is not None:
            self.auto_scaling_spot_with_limit_allowed = m.get('AutoScalingSpotWithLimitAllowed')
        if m.get('AutoScalingVersion') is not None:
            self.auto_scaling_version = m.get('AutoScalingVersion')
        if m.get('AutoScalingWithGraceAllowed') is not None:
            self.auto_scaling_with_grace_allowed = m.get('AutoScalingWithGraceAllowed')
        if m.get('BootstrapActionList') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoBootstrapActionList()
            self.bootstrap_action_list = temp_model.from_map(m['BootstrapActionList'])
        if m.get('BootstrapFailed') is not None:
            self.bootstrap_failed = m.get('BootstrapFailed')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Configurations') is not None:
            self.configurations = m.get('Configurations')
        if m.get('CoreNodeInService') is not None:
            self.core_node_in_service = m.get('CoreNodeInService')
        if m.get('CoreNodeTotal') is not None:
            self.core_node_total = m.get('CoreNodeTotal')
        if m.get('CreateResource') is not None:
            self.create_resource = m.get('CreateResource')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('EasEnable') is not None:
            self.eas_enable = m.get('EasEnable')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('FailReason') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoFailReason()
            self.fail_reason = temp_model.from_map(m['FailReason'])
        if m.get('GatewayClusterIds') is not None:
            self.gateway_cluster_ids = m.get('GatewayClusterIds')
        if m.get('GatewayClusterInfoList') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoGatewayClusterInfoList()
            self.gateway_cluster_info_list = temp_model.from_map(m['GatewayClusterInfoList'])
        if m.get('HighAvailabilityEnable') is not None:
            self.high_availability_enable = m.get('HighAvailabilityEnable')
        if m.get('HostGroupList') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostGroupList()
            self.host_group_list = temp_model.from_map(m['HostGroupList'])
        if m.get('HostPoolInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoHostPoolInfo()
            self.host_pool_info = temp_model.from_map(m['HostPoolInfo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('LocalMetaDb') is not None:
            self.local_meta_db = m.get('LocalMetaDb')
        if m.get('LogEnable') is not None:
            self.log_enable = m.get('LogEnable')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MasterNodeInService') is not None:
            self.master_node_in_service = m.get('MasterNodeInService')
        if m.get('MasterNodeTotal') is not None:
            self.master_node_total = m.get('MasterNodeTotal')
        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelateClusterId') is not None:
            self.relate_cluster_id = m.get('RelateClusterId')
        if m.get('RelateClusterInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoRelateClusterInfo()
            self.relate_cluster_info = temp_model.from_map(m['RelateClusterInfo'])
        if m.get('ResizeDiskEnable') is not None:
            self.resize_disk_enable = m.get('ResizeDiskEnable')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('ShowSoftwareInterface') is not None:
            self.show_software_interface = m.get('ShowSoftwareInterface')
        if m.get('SoftwareInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfoSoftwareInfo()
            self.software_info = temp_model.from_map(m['SoftwareInfo'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('TaskNodeInService') is not None:
            self.task_node_in_service = m.get('TaskNodeInService')
        if m.get('TaskNodeTotal') is not None:
            self.task_node_total = m.get('TaskNodeTotal')
        if m.get('UserDefinedEmrEcsRole') is not None:
            self.user_defined_emr_ecs_role = m.get('UserDefinedEmrEcsRole')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeClusterV2ResponseBody(TeaModel):
    def __init__(
        self,
        cluster_info: DescribeClusterV2ResponseBodyClusterInfo = None,
        request_id: str = None,
    ):
        self.cluster_info = cluster_info
        self.request_id = request_id

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeClusterV2ResponseBodyClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterV2ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeClusterV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowResponseBodyParentFlowListParentFlow(TeaModel):
    def __init__(
        self,
        parent_flow_id: str = None,
        parent_flow_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.parent_flow_id = parent_flow_id
        self.parent_flow_name = parent_flow_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_flow_id is not None:
            result['ParentFlowId'] = self.parent_flow_id
        if self.parent_flow_name is not None:
            result['ParentFlowName'] = self.parent_flow_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentFlowId') is not None:
            self.parent_flow_id = m.get('ParentFlowId')
        if m.get('ParentFlowName') is not None:
            self.parent_flow_name = m.get('ParentFlowName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class DescribeFlowResponseBodyParentFlowList(TeaModel):
    def __init__(
        self,
        parent_flow: List[DescribeFlowResponseBodyParentFlowListParentFlow] = None,
    ):
        self.parent_flow = parent_flow

    def validate(self):
        if self.parent_flow:
            for k in self.parent_flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParentFlow'] = []
        if self.parent_flow is not None:
            for k in self.parent_flow:
                result['ParentFlow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parent_flow = []
        if m.get('ParentFlow') is not None:
            for k in m.get('ParentFlow'):
                temp_model = DescribeFlowResponseBodyParentFlowListParentFlow()
                self.parent_flow.append(temp_model.from_map(k))
        return self


class DescribeFlowResponseBody(TeaModel):
    def __init__(
        self,
        alert_conf: str = None,
        alert_ding_ding_group_biz_id: str = None,
        alert_user_group_biz_id: str = None,
        application: str = None,
        category_id: str = None,
        cluster_id: str = None,
        create_cluster: bool = None,
        cron_expr: str = None,
        description: str = None,
        edit_lock_detail: str = None,
        end_schedule: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        graph: str = None,
        host_name: str = None,
        id: str = None,
        name: str = None,
        namespace: str = None,
        parent_flow_list: DescribeFlowResponseBodyParentFlowList = None,
        periodic: bool = None,
        request_id: str = None,
        start_schedule: int = None,
        status: str = None,
        type: str = None,
    ):
        self.alert_conf = alert_conf
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id
        self.alert_user_group_biz_id = alert_user_group_biz_id
        self.application = application
        self.category_id = category_id
        self.cluster_id = cluster_id
        self.create_cluster = create_cluster
        self.cron_expr = cron_expr
        self.description = description
        self.edit_lock_detail = edit_lock_detail
        self.end_schedule = end_schedule
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.graph = graph
        self.host_name = host_name
        self.id = id
        self.name = name
        self.namespace = namespace
        self.parent_flow_list = parent_flow_list
        self.periodic = periodic
        self.request_id = request_id
        self.start_schedule = start_schedule
        self.status = status
        self.type = type

    def validate(self):
        if self.parent_flow_list:
            self.parent_flow_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.application is not None:
            result['Application'] = self.application
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.edit_lock_detail is not None:
            result['EditLockDetail'] = self.edit_lock_detail
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list.to_map()
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('Application') is not None:
            self.application = m.get('Application')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditLockDetail') is not None:
            self.edit_lock_detail = m.get('EditLockDetail')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentFlowList') is not None:
            temp_model = DescribeFlowResponseBodyParentFlowList()
            self.parent_flow_list = temp_model.from_map(m['ParentFlowList'])
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowCategoryTreeRequest(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        keyword: str = None,
        mode: str = None,
        project_id: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.category_id = category_id
        self.keyword = keyword
        self.mode = mode
        self.project_id = project_id
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowCategoryTreeResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowCategoryTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowCategoryTreeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeFlowCategoryTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowJobRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.id = id
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowJobResponseBodyResourceListResource(TeaModel):
    def __init__(
        self,
        alias: str = None,
        path: str = None,
    ):
        # 保留参数。
        self.alias = alias
        # 保留参数。
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeFlowJobResponseBodyResourceList(TeaModel):
    def __init__(
        self,
        resource: List[DescribeFlowJobResponseBodyResourceListResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeFlowJobResponseBodyResourceListResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeFlowJobResponseBody(TeaModel):
    def __init__(
        self,
        adhoc: str = None,
        alert_conf: str = None,
        category_id: str = None,
        custom_variables: str = None,
        description: str = None,
        edit_lock_detail: str = None,
        env_conf: str = None,
        fail_act: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        knox_password: str = None,
        knox_user: str = None,
        last_instance_id: str = None,
        max_retry: int = None,
        max_running_time_sec: int = None,
        mode: str = None,
        monitor_conf: str = None,
        name: str = None,
        param_conf: str = None,
        params: str = None,
        request_id: str = None,
        resource_list: DescribeFlowJobResponseBodyResourceList = None,
        retry_interval: int = None,
        retry_policy: str = None,
        run_conf: str = None,
        type: str = None,
    ):
        # 是否临时查询。
        self.adhoc = adhoc
        # 报警配置。
        self.alert_conf = alert_conf
        # 作业所在目录ID。
        self.category_id = category_id
        # 自定义变量。
        self.custom_variables = custom_variables
        # 作业的描述。
        self.description = description
        # 保留参数。
        self.edit_lock_detail = edit_lock_detail
        # 环境变量设置。
        self.env_conf = env_conf
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act
        # 创建时间。
        self.gmt_create = gmt_create
        # 最后修改时间。
        self.gmt_modified = gmt_modified
        # 作业ID。
        self.id = id
        # Knox的用户密码，执行Zeppelin Notebook时必须提供。
        self.knox_password = knox_password
        # Knox的用户名，执行Zeppelin Notebook时必须提供。
        self.knox_user = knox_user
        # 最后一次执行的实例ID。
        self.last_instance_id = last_instance_id
        # 最大重试次数。
        self.max_retry = max_retry
        # 保留参数。
        self.max_running_time_sec = max_running_time_sec
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf
        # 作业名称。
        self.name = name
        # 参数设置。
        self.param_conf = param_conf
        # 作业内容。
        self.params = params
        # 请求ID。
        self.request_id = request_id
        self.resource_list = resource_list
        # 重试间隔 0~300（秒）。
        self.retry_interval = retry_interval
        # 重试策略，保留参数。
        self.retry_policy = retry_policy
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
        self.type = type

    def validate(self):
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.edit_lock_detail is not None:
            result['EditLockDetail'] = self.edit_lock_detail
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.knox_password is not None:
            result['KnoxPassword'] = self.knox_password
        if self.knox_user is not None:
            result['KnoxUser'] = self.knox_user
        if self.last_instance_id is not None:
            result['LastInstanceId'] = self.last_instance_id
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.max_running_time_sec is not None:
            result['MaxRunningTimeSec'] = self.max_running_time_sec
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list.to_map()
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EditLockDetail') is not None:
            self.edit_lock_detail = m.get('EditLockDetail')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KnoxPassword') is not None:
            self.knox_password = m.get('KnoxPassword')
        if m.get('KnoxUser') is not None:
            self.knox_user = m.get('KnoxUser')
        if m.get('LastInstanceId') is not None:
            self.last_instance_id = m.get('LastInstanceId')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('MaxRunningTimeSec') is not None:
            self.max_running_time_sec = m.get('MaxRunningTimeSec')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceList') is not None:
            temp_model = DescribeFlowJobResponseBodyResourceList()
            self.resource_list = temp_model.from_map(m['ResourceList'])
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowNodeInstanceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowNodeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        adhoc: bool = None,
        cluster_id: str = None,
        cluster_name: str = None,
        duration: int = None,
        end_time: int = None,
        env_conf: str = None,
        external_child_ids: str = None,
        external_id: str = None,
        external_info: str = None,
        external_status: str = None,
        external_sub_id: str = None,
        fail_act: str = None,
        flow_id: str = None,
        flow_instance_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        host_name: str = None,
        id: str = None,
        job_id: str = None,
        job_name: str = None,
        job_params: str = None,
        job_type: str = None,
        max_retry: str = None,
        mode: str = None,
        monitor_conf: str = None,
        node_name: str = None,
        param_conf: str = None,
        pending: bool = None,
        project_id: str = None,
        request_id: str = None,
        retries: int = None,
        retry_interval: str = None,
        retry_policy: str = None,
        run_conf: str = None,
        start_time: int = None,
        status: str = None,
        type: str = None,
    ):
        self.adhoc = adhoc
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.duration = duration
        self.end_time = end_time
        self.env_conf = env_conf
        self.external_child_ids = external_child_ids
        self.external_id = external_id
        self.external_info = external_info
        self.external_status = external_status
        self.external_sub_id = external_sub_id
        self.fail_act = fail_act
        self.flow_id = flow_id
        self.flow_instance_id = flow_instance_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.host_name = host_name
        self.id = id
        self.job_id = job_id
        self.job_name = job_name
        self.job_params = job_params
        self.job_type = job_type
        self.max_retry = max_retry
        self.mode = mode
        self.monitor_conf = monitor_conf
        self.node_name = node_name
        self.param_conf = param_conf
        self.pending = pending
        self.project_id = project_id
        self.request_id = request_id
        self.retries = retries
        self.retry_interval = retry_interval
        self.retry_policy = retry_policy
        self.run_conf = run_conf
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.external_child_ids is not None:
            result['ExternalChildIds'] = self.external_child_ids
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info
        if self.external_status is not None:
            result['ExternalStatus'] = self.external_status
        if self.external_sub_id is not None:
            result['ExternalSubId'] = self.external_sub_id
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_params is not None:
            result['JobParams'] = self.job_params
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retries is not None:
            result['Retries'] = self.retries
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('ExternalChildIds') is not None:
            self.external_child_ids = m.get('ExternalChildIds')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ExternalInfo') is not None:
            self.external_info = m.get('ExternalInfo')
        if m.get('ExternalStatus') is not None:
            self.external_status = m.get('ExternalStatus')
        if m.get('ExternalSubId') is not None:
            self.external_sub_id = m.get('ExternalSubId')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Retries') is not None:
            self.retries = m.get('Retries')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowNodeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowNodeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeFlowNodeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        region_id: str = None,
    ):
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowProjectResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        user_id: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.request_id = request_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeFlowProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLibraryDetailRequest(TeaModel):
    def __init__(
        self,
        library_biz_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.library_biz_id = library_biz_id
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeLibraryDetailResponseBody(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        library_version: str = None,
        name: str = None,
        properties: str = None,
        request_id: str = None,
        scope: str = None,
        source_location: str = None,
        source_type: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.library_version = library_version
        self.name = name
        self.properties = properties
        self.request_id = request_id
        self.scope = scope
        self.source_location = source_location
        self.source_type = source_type
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.library_version is not None:
            result['LibraryVersion'] = self.library_version
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LibraryVersion') is not None:
            self.library_version = m.get('LibraryVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeLibraryDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLibraryDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeLibraryDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLibraryInstallTaskDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_owner_id: int = None,
        task_biz_id: str = None,
    ):
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.task_biz_id = task_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_biz_id is not None:
            result['TaskBizId'] = self.task_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskBizId') is not None:
            self.task_biz_id = m.get('TaskBizId')
        return self


class DescribeLibraryInstallTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        detail: str = None,
        end_time: int = None,
        execute_time: int = None,
        hostname: str = None,
        library_biz_id: str = None,
        request_id: str = None,
        start_time: int = None,
        task_group_id: str = None,
        task_id: str = None,
        task_process: int = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.detail = detail
        self.end_time = end_time
        self.execute_time = execute_time
        self.hostname = hostname
        self.library_biz_id = library_biz_id
        self.request_id = request_id
        self.start_time = start_time
        self.task_group_id = task_group_id
        self.task_id = task_id
        self.task_process = task_process
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_process is not None:
            result['TaskProcess'] = self.task_process
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProcess') is not None:
            self.task_process = m.get('TaskProcess')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeLibraryInstallTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLibraryInstallTaskDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeLibraryInstallTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallLibrariesRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id_list: List[str] = None,
        library_biz_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.cluster_biz_id_list = cluster_biz_id_list
        self.library_biz_id = library_biz_id
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id_list is not None:
            result['ClusterBizIdList'] = self.cluster_biz_id_list
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizIdList') is not None:
            self.cluster_biz_id_list = m.get('ClusterBizIdList')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class InstallLibrariesResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InstallLibrariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallLibrariesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = InstallLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillFlowJobRequest(TeaModel):
    def __init__(
        self,
        job_instance_id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # 作业实例ID。您可以调用DescribeFlowJob查看作业实例ID。
        self.job_instance_id = job_instance_id
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_instance_id is not None:
            result['JobInstanceId'] = self.job_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInstanceId') is not None:
            self.job_instance_id = m.get('JobInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class KillFlowJobResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # 返回执行结果，包含如下：true（执行成功），false（执行失败）
        self.data = data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = KillFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_type_list: List[str] = None,
        create_type: str = None,
        default_status: bool = None,
        deposit_type: str = None,
        expired_tag_list: List[str] = None,
        is_desc: bool = None,
        machine_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        status_list: List[str] = None,
        tag: List[ListClustersRequestTag] = None,
    ):
        self.cluster_type_list = cluster_type_list
        self.create_type = create_type
        self.default_status = default_status
        self.deposit_type = deposit_type
        self.expired_tag_list = expired_tag_list
        self.is_desc = is_desc
        self.machine_type = machine_type
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.status_list = status_list
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type_list is not None:
            result['ClusterTypeList'] = self.cluster_type_list
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.default_status is not None:
            result['DefaultStatus'] = self.default_status
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.expired_tag_list is not None:
            result['ExpiredTagList'] = self.expired_tag_list
        if self.is_desc is not None:
            result['IsDesc'] = self.is_desc
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterTypeList') is not None:
            self.cluster_type_list = m.get('ClusterTypeList')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DefaultStatus') is not None:
            self.default_status = m.get('DefaultStatus')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('ExpiredTagList') is not None:
            self.expired_tag_list = m.get('ExpiredTagList')
        if m.get('IsDesc') is not None:
            self.is_desc = m.get('IsDesc')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListClustersResponseBodyClustersClusterInfoFailReason(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClustersResponseBodyClustersClusterInfoOrderTaskInfo(TeaModel):
    def __init__(
        self,
        current_count: int = None,
        order_id_list: str = None,
        target_count: int = None,
    ):
        self.current_count = current_count
        self.order_id_list = order_id_list
        self.target_count = target_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.order_id_list is not None:
            result['OrderIdList'] = self.order_id_list
        if self.target_count is not None:
            result['TargetCount'] = self.target_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('OrderIdList') is not None:
            self.order_id_list = m.get('OrderIdList')
        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')
        return self


class ListClustersResponseBodyClustersClusterInfoTagsTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListClustersResponseBodyClustersClusterInfoTags(TeaModel):
    def __init__(
        self,
        tag: List[ListClustersResponseBodyClustersClusterInfoTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListClustersResponseBodyClustersClusterInfoTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        create_resource: str = None,
        create_time: int = None,
        deposit_type: str = None,
        expired_time: int = None,
        fail_reason: ListClustersResponseBodyClustersClusterInfoFailReason = None,
        has_uncompleted_order: bool = None,
        id: str = None,
        k_8s_cluster_id: str = None,
        machine_type: str = None,
        meta_store_type: str = None,
        name: str = None,
        order_list: str = None,
        order_task_info: ListClustersResponseBodyClustersClusterInfoOrderTaskInfo = None,
        period: int = None,
        running_time: int = None,
        status: str = None,
        tags: ListClustersResponseBodyClustersClusterInfoTags = None,
        type: str = None,
    ):
        self.charge_type = charge_type
        self.create_resource = create_resource
        self.create_time = create_time
        self.deposit_type = deposit_type
        self.expired_time = expired_time
        self.fail_reason = fail_reason
        self.has_uncompleted_order = has_uncompleted_order
        self.id = id
        self.k_8s_cluster_id = k_8s_cluster_id
        self.machine_type = machine_type
        self.meta_store_type = meta_store_type
        self.name = name
        self.order_list = order_list
        self.order_task_info = order_task_info
        self.period = period
        self.running_time = running_time
        self.status = status
        self.tags = tags
        self.type = type

    def validate(self):
        if self.fail_reason:
            self.fail_reason.validate()
        if self.order_task_info:
            self.order_task_info.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_resource is not None:
            result['CreateResource'] = self.create_resource
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deposit_type is not None:
            result['DepositType'] = self.deposit_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason.to_map()
        if self.has_uncompleted_order is not None:
            result['HasUncompletedOrder'] = self.has_uncompleted_order
        if self.id is not None:
            result['Id'] = self.id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.meta_store_type is not None:
            result['MetaStoreType'] = self.meta_store_type
        if self.name is not None:
            result['Name'] = self.name
        if self.order_list is not None:
            result['OrderList'] = self.order_list
        if self.order_task_info is not None:
            result['OrderTaskInfo'] = self.order_task_info.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateResource') is not None:
            self.create_resource = m.get('CreateResource')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DepositType') is not None:
            self.deposit_type = m.get('DepositType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FailReason') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoFailReason()
            self.fail_reason = temp_model.from_map(m['FailReason'])
        if m.get('HasUncompletedOrder') is not None:
            self.has_uncompleted_order = m.get('HasUncompletedOrder')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MetaStoreType') is not None:
            self.meta_store_type = m.get('MetaStoreType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderList') is not None:
            self.order_list = m.get('OrderList')
        if m.get('OrderTaskInfo') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoOrderTaskInfo()
            self.order_task_info = temp_model.from_map(m['OrderTaskInfo'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            temp_model = ListClustersResponseBodyClustersClusterInfoTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_info: List[ListClustersResponseBodyClustersClusterInfo] = None,
    ):
        self.cluster_info = cluster_info

    def validate(self):
        if self.cluster_info:
            for k in self.cluster_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterInfo'] = []
        if self.cluster_info is not None:
            for k in self.cluster_info:
                result['ClusterInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_info = []
        if m.get('ClusterInfo') is not None:
            for k in m.get('ClusterInfo'):
                temp_model = ListClustersResponseBodyClustersClusterInfo()
                self.cluster_info.append(temp_model.from_map(k))
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: ListClustersResponseBodyClusters = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.clusters = clusters
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.clusters:
            self.clusters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = ListClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ListFlowRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        id: str = None,
        job_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        periodic: bool = None,
        project_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id
        # 工作流ID。您可以调用ListFlowInstance查看工作流ID。
        self.id = id
        # 作业ID。您可以调用ListFlowJob查看。
        self.job_id = job_id
        # 工作流名称。您可以调用ListFlowInstance查看。
        self.name = name
        # 页码。
        self.page_number = page_number
        # 每页查询数量。
        self.page_size = page_size
        # 是否调度。
        self.periodic = periodic
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id
        # 状态：  STOP_SCHEDULE（停止调度） UNDER_SCHEDULE（调度中）
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
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFlowResponseBodyFlowFlow(TeaModel):
    def __init__(
        self,
        alert_conf: str = None,
        alert_ding_ding_group_biz_id: str = None,
        alert_user_group_biz_id: str = None,
        category_id: str = None,
        cluster_id: str = None,
        create_cluster: bool = None,
        cron_expr: str = None,
        description: str = None,
        end_schedule: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        graph: str = None,
        host_name: str = None,
        id: str = None,
        name: str = None,
        periodic: bool = None,
        project_id: str = None,
        start_schedule: int = None,
        status: str = None,
        type: str = None,
    ):
        self.alert_conf = alert_conf
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id
        self.alert_user_group_biz_id = alert_user_group_biz_id
        self.category_id = category_id
        self.cluster_id = cluster_id
        self.create_cluster = create_cluster
        self.cron_expr = cron_expr
        self.description = description
        self.end_schedule = end_schedule
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.graph = graph
        self.host_name = host_name
        self.id = id
        self.name = name
        self.periodic = periodic
        self.project_id = project_id
        self.start_schedule = start_schedule
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowResponseBodyFlow(TeaModel):
    def __init__(
        self,
        flow: List[ListFlowResponseBodyFlowFlow] = None,
    ):
        self.flow = flow

    def validate(self):
        if self.flow:
            for k in self.flow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Flow'] = []
        if self.flow is not None:
            for k in self.flow:
                result['Flow'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow = []
        if m.get('Flow') is not None:
            for k in m.get('Flow'):
                temp_model = ListFlowResponseBodyFlowFlow()
                self.flow.append(temp_model.from_map(k))
        return self


class ListFlowResponseBody(TeaModel):
    def __init__(
        self,
        flow: ListFlowResponseBodyFlow = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 工作流列表
        self.flow = flow
        # 页码。
        self.page_number = page_number
        # 每页数量。
        self.page_size = page_size
        # 请求ID。
        self.request_id = request_id
        # 总数。
        self.total = total

    def validate(self):
        if self.flow:
            self.flow.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['Flow'] = self.flow.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            temp_model = ListFlowResponseBodyFlow()
            self.flow = temp_model.from_map(m['Flow'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowJobHistoryRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        job_type: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        region_id: str = None,
        status_list: List[str] = None,
        time_range: str = None,
    ):
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.id = id
        # 作业实例ID。您可以调用DescribeFlowJob查看作业实例ID。
        self.instance_id = instance_id
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
        self.job_type = job_type
        # 当前页码。
        self.page_number = page_number
        # 分页查询时每页行数。
        self.page_size = page_size
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id
        # 状态列表。取值如下：SUBMITTED, RUNNING, SUCCESS, FAILED, KILL_FAILED, KILL_SUCCESS
        self.status_list = status_list
        # 查询的时间范围参数，参数列表：type: range，from: 开始时间（long型时间戳），to: 结束时间（long型时间戳）
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        end_time: int = None,
        env_conf: str = None,
        external_id: str = None,
        external_info: str = None,
        external_status: str = None,
        fail_act: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        host_name: str = None,
        id: str = None,
        job_id: str = None,
        job_name: str = None,
        job_params: str = None,
        job_type: str = None,
        max_retry: int = None,
        node_name: str = None,
        param_conf: str = None,
        project_id: str = None,
        retries: int = None,
        retry_interval: int = None,
        run_conf: str = None,
        start_time: int = None,
        status: str = None,
        type: str = None,
        pending: bool = None,
    ):
        # 集群ID。
        self.cluster_id = cluster_id
        # 运行结束时间。
        self.end_time = end_time
        # 环境变量设置。
        self.env_conf = env_conf
        # 启动器的application的ID。
        self.external_id = external_id
        # 外部信息。例如，运行作业的错误诊断信息。
        self.external_info = external_info
        # 实例对应的Container的状态：SUBMITTED, RUNNING, SUCCESS, FAIL, KILL_FAIL, KILL_SUCCESS
        self.external_status = external_status
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act
        # 创建时间。
        self.gmt_create = gmt_create
        # 创建时间。
        self.gmt_modified = gmt_modified
        # 保留参数。
        self.host_name = host_name
        # 作业实例ID。
        self.id = id
        # 作业ID。
        self.job_id = job_id
        # 作业名称。
        self.job_name = job_name
        # 作业内容。
        self.job_params = job_params
        # 作业类型。
        self.job_type = job_type
        # 最大重试次数。
        self.max_retry = max_retry
        # 保留参数。
        self.node_name = node_name
        # 参数设置。
        self.param_conf = param_conf
        # 项目ID。
        self.project_id = project_id
        # 重试次数。
        self.retries = retries
        # 重试间隔 0-300（秒）。
        self.retry_interval = retry_interval
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf
        # 运行开始时间。
        self.start_time = start_time
        # 实例的执行状态：PREP：准备启动，SUBMITTING：提交中，RUNNING：运行中DONE：已完成，OK：执行成功，FAILED：执行失败，KILLED：已终止，KILL_FAILED：终止失败，START_RETRY：开始重试
        self.status = status
        # 节点类型：JOB：作业，CLUSTER：集群，START：开始，END：结束
        self.type = type
        # 是否结束。
        self.pending = pending

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info
        if self.external_status is not None:
            result['ExternalStatus'] = self.external_status
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_params is not None:
            result['JobParams'] = self.job_params
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.retries is not None:
            result['Retries'] = self.retries
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.pending is not None:
            result['pending'] = self.pending
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ExternalInfo') is not None:
            self.external_info = m.get('ExternalInfo')
        if m.get('ExternalStatus') is not None:
            self.external_status = m.get('ExternalStatus')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Retries') is not None:
            self.retries = m.get('Retries')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('pending') is not None:
            self.pending = m.get('pending')
        return self


class ListFlowJobHistoryResponseBodyNodeInstances(TeaModel):
    def __init__(
        self,
        node_instance: List[ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance] = None,
    ):
        self.node_instance = node_instance

    def validate(self):
        if self.node_instance:
            for k in self.node_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstance'] = []
        if self.node_instance is not None:
            for k in self.node_instance:
                result['NodeInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_instance = []
        if m.get('NodeInstance') is not None:
            for k in m.get('NodeInstance'):
                temp_model = ListFlowJobHistoryResponseBodyNodeInstancesNodeInstance()
                self.node_instance.append(temp_model.from_map(k))
        return self


class ListFlowJobHistoryResponseBody(TeaModel):
    def __init__(
        self,
        node_instances: ListFlowJobHistoryResponseBodyNodeInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 作业实例列表。
        self.node_instances = node_instances
        # 当前页码。
        self.page_number = page_number
        # 分页查询时设置的每页行数。
        self.page_size = page_size
        # 请求ID。
        self.request_id = request_id
        # 记录总数。
        self.total = total

    def validate(self):
        if self.node_instances:
            self.node_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_instances is not None:
            result['NodeInstances'] = self.node_instances.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeInstances') is not None:
            temp_model = ListFlowJobHistoryResponseBodyNodeInstances()
            self.node_instances = temp_model.from_map(m['NodeInstances'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowJobHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowJobHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFlowJobHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowJobsRequest(TeaModel):
    def __init__(
        self,
        adhoc: bool = None,
        exact_name: str = None,
        id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # 是否为临时查询。用于过滤作业。
        self.adhoc = adhoc
        self.exact_name = exact_name
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.id = id
        # 作业名称。
        self.name = name
        # 当前页数。
        self.page_number = page_number
        # 每页的作业数量。
        self.page_size = page_size
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id
        # 作业类型。用于过滤作业，支持的类型有：SPARK，SPARK_STREAMING，ZEPPELIN。
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.exact_name is not None:
            result['ExactName'] = self.exact_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('ExactName') is not None:
            self.exact_name = m.get('ExactName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowJobsResponseBodyJobListJobResourceListResource(TeaModel):
    def __init__(
        self,
        alias: str = None,
        path: str = None,
    ):
        # 保留参数。
        self.alias = alias
        # 保留参数。
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListFlowJobsResponseBodyJobListJobResourceList(TeaModel):
    def __init__(
        self,
        resource: List[ListFlowJobsResponseBodyJobListJobResourceListResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = ListFlowJobsResponseBodyJobListJobResourceListResource()
                self.resource.append(temp_model.from_map(k))
        return self


class ListFlowJobsResponseBodyJobListJob(TeaModel):
    def __init__(
        self,
        adhoc: str = None,
        alert_conf: str = None,
        category_id: str = None,
        custom_variables: str = None,
        description: str = None,
        env_conf: str = None,
        fail_act: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        last_instance_detail: str = None,
        max_retry: int = None,
        mode: str = None,
        monitor_conf: str = None,
        name: str = None,
        param_conf: str = None,
        params: str = None,
        resource_list: ListFlowJobsResponseBodyJobListJobResourceList = None,
        retry_interval: int = None,
        run_conf: str = None,
        type: str = None,
    ):
        # 是否临时查询。
        self.adhoc = adhoc
        # 报警配置。
        self.alert_conf = alert_conf
        # 作业所在目录ID。
        self.category_id = category_id
        # 自定义变量。
        self.custom_variables = custom_variables
        # 作业的描述。
        self.description = description
        # 环境变量设置。
        self.env_conf = env_conf
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act
        # 创建时间。
        self.gmt_create = gmt_create
        # 最后修改时间。
        self.gmt_modified = gmt_modified
        # 作业ID。
        self.id = id
        # 最后一次执行的实例ID。
        self.last_instance_detail = last_instance_detail
        # 最大重试次数。
        self.max_retry = max_retry
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf
        # 作业名称。
        self.name = name
        # 参数设置。
        self.param_conf = param_conf
        # 作业内容。
        self.params = params
        self.resource_list = resource_list
        # 重试间隔 0~300（秒）。
        self.retry_interval = retry_interval
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf
        # 作业的类型，可能的取值有：SPARK，SPARK_STREAMING，ZEPPELIN
        self.type = type

    def validate(self):
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adhoc is not None:
            result['Adhoc'] = self.adhoc
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.last_instance_detail is not None:
            result['LastInstanceDetail'] = self.last_instance_detail
        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list.to_map()
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adhoc') is not None:
            self.adhoc = m.get('Adhoc')
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastInstanceDetail') is not None:
            self.last_instance_detail = m.get('LastInstanceDetail')
        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ResourceList') is not None:
            temp_model = ListFlowJobsResponseBodyJobListJobResourceList()
            self.resource_list = temp_model.from_map(m['ResourceList'])
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowJobsResponseBodyJobList(TeaModel):
    def __init__(
        self,
        job: List[ListFlowJobsResponseBodyJobListJob] = None,
    ):
        self.job = job

    def validate(self):
        if self.job:
            for k in self.job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Job'] = []
        if self.job is not None:
            for k in self.job:
                result['Job'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job = []
        if m.get('Job') is not None:
            for k in m.get('Job'):
                temp_model = ListFlowJobsResponseBodyJobListJob()
                self.job.append(temp_model.from_map(k))
        return self


class ListFlowJobsResponseBody(TeaModel):
    def __init__(
        self,
        job_list: ListFlowJobsResponseBodyJobList = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.job_list = job_list
        # 当前页数。
        self.page_number = page_number
        # 每页的作业数量。
        self.page_size = page_size
        # 请求ID。
        self.request_id = request_id
        # 作业数量。
        self.total = total

    def validate(self):
        if self.job_list:
            self.job_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_list is not None:
            result['JobList'] = self.job_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobList') is not None:
            temp_model = ListFlowJobsResponseBodyJobList()
            self.job_list = temp_model.from_map(m['JobList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFlowJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowProjectUserRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListFlowProjectUserResponseBodyUsersUser(TeaModel):
    def __init__(
        self,
        account_user_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        owner_id: str = None,
        project_id: str = None,
        user_name: str = None,
    ):
        self.account_user_id = account_user_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.project_id = project_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_user_id is not None:
            result['AccountUserId'] = self.account_user_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUserId') is not None:
            self.account_user_id = m.get('AccountUserId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListFlowProjectUserResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user: List[ListFlowProjectUserResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListFlowProjectUserResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListFlowProjectUserResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        users: ListFlowProjectUserResponseBodyUsers = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total = total
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Users') is not None:
            temp_model = ListFlowProjectUserResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class ListFlowProjectUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowProjectUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFlowProjectUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowProjectsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        project_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # 项目名称，用于过滤项目
        self.name = name
        # 页码，用于分页
        self.page_number = page_number
        # 每页数量
        self.page_size = page_size
        # 产品类型。固定值DATABIRCKS_DATAINSIGHT
        self.product_type = product_type
        # 项目ID。您可以调用ListFlowProjects查看项目的ID
        self.project_id = project_id
        # 地域ID
        self.region_id = region_id
        # 资源组ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFlowProjectsResponseBodyProjectsProject(TeaModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 项目描述
        self.description = description
        # 创建时间戳
        self.gmt_create = gmt_create
        # 修改时间戳
        self.gmt_modified = gmt_modified
        # 项目ID
        self.id = id
        # 项目名称
        self.name = name
        # 主账号ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListFlowProjectsResponseBodyProjects(TeaModel):
    def __init__(
        self,
        project: List[ListFlowProjectsResponseBodyProjectsProject] = None,
    ):
        self.project = project

    def validate(self):
        if self.project:
            for k in self.project:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Project'] = []
        if self.project is not None:
            for k in self.project:
                result['Project'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project = []
        if m.get('Project') is not None:
            for k in m.get('Project'):
                temp_model = ListFlowProjectsResponseBodyProjectsProject()
                self.project.append(temp_model.from_map(k))
        return self


class ListFlowProjectsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        projects: ListFlowProjectsResponseBodyProjects = None,
        request_id: str = None,
        total: int = None,
    ):
        # 页码
        self.page_number = page_number
        # 每页数量
        self.page_size = page_size
        # 项目列表
        self.projects = projects
        # 请求ID
        self.request_id = request_id
        # 总数
        self.total = total

    def validate(self):
        if self.projects:
            self.projects.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.projects is not None:
            result['Projects'] = self.projects.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Projects') is not None:
            temp_model = ListFlowProjectsResponseBodyProjects()
            self.projects = temp_model.from_map(m['Projects'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListFlowProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListFlowProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLibrariesRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        current_size: int = None,
        limit: int = None,
        order_field: str = None,
        order_mode: str = None,
        page_count: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.current_size = current_size
        self.limit = limit
        self.order_field = order_field
        self.order_mode = order_mode
        self.page_count = page_count
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListLibrariesResponseBodyItemsItem(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        library_version: str = None,
        name: str = None,
        properties: str = None,
        scope: str = None,
        source_location: str = None,
        source_type: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.library_version = library_version
        self.name = name
        self.properties = properties
        self.scope = scope
        self.source_location = source_location
        self.source_type = source_type
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.library_version is not None:
            result['LibraryVersion'] = self.library_version
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.source_location is not None:
            result['SourceLocation'] = self.source_location
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LibraryVersion') is not None:
            self.library_version = m.get('LibraryVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListLibrariesResponseBodyItems(TeaModel):
    def __init__(
        self,
        item: List[ListLibrariesResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ListLibrariesResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListLibrariesResponseBody(TeaModel):
    def __init__(
        self,
        items: ListLibrariesResponseBodyItems = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('Items') is not None:
            temp_model = ListLibrariesResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLibrariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLibrariesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLibraryInstallTasksRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        current_size: int = None,
        library_biz_id: str = None,
        limit: int = None,
        order_field: str = None,
        order_mode: str = None,
        page_count: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.current_size = current_size
        self.library_biz_id = library_biz_id
        self.limit = limit
        self.order_field = order_field
        self.order_mode = order_mode
        self.page_count = page_count
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListLibraryInstallTasksResponseBodyItemsItem(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        detail: str = None,
        end_time: int = None,
        execute_time: int = None,
        hostname: str = None,
        library_biz_id: str = None,
        start_time: int = None,
        task_group_id: str = None,
        task_id: str = None,
        task_process: int = None,
        task_status: str = None,
        task_type: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.detail = detail
        self.end_time = end_time
        self.execute_time = execute_time
        self.hostname = hostname
        self.library_biz_id = library_biz_id
        self.start_time = start_time
        self.task_group_id = task_group_id
        self.task_id = task_id
        self.task_process = task_process
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_process is not None:
            result['TaskProcess'] = self.task_process
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskProcess') is not None:
            self.task_process = m.get('TaskProcess')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListLibraryInstallTasksResponseBodyItems(TeaModel):
    def __init__(
        self,
        item: List[ListLibraryInstallTasksResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ListLibraryInstallTasksResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListLibraryInstallTasksResponseBody(TeaModel):
    def __init__(
        self,
        items: ListLibraryInstallTasksResponseBodyItems = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('Items') is not None:
            temp_model = ListLibraryInstallTasksResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLibraryInstallTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLibraryInstallTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLibraryInstallTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLibraryStatusRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        current_size: int = None,
        library_biz_id: str = None,
        limit: int = None,
        order_field: str = None,
        order_mode: str = None,
        page_count: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.current_size = current_size
        self.library_biz_id = library_biz_id
        self.limit = limit
        self.order_field = order_field
        self.order_mode = order_mode
        self.page_count = page_count
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.current_size is not None:
            result['CurrentSize'] = self.current_size
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('CurrentSize') is not None:
            self.current_size = m.get('CurrentSize')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListLibraryStatusResponseBodyItemsItem(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        cluster_name: str = None,
        library_biz_id: str = None,
        library_name: str = None,
        status: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.cluster_name = cluster_name
        self.library_biz_id = library_biz_id
        self.library_name = library_name
        self.status = status

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
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.library_name is not None:
            result['LibraryName'] = self.library_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('LibraryName') is not None:
            self.library_name = m.get('LibraryName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLibraryStatusResponseBodyItems(TeaModel):
    def __init__(
        self,
        item: List[ListLibraryStatusResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ListLibraryStatusResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class ListLibraryStatusResponseBody(TeaModel):
    def __init__(
        self,
        items: ListLibraryStatusResponseBodyItems = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('Items') is not None:
            temp_model = ListLibraryStatusResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLibraryStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLibraryStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListLibraryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # 资源组ID
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        # 标签
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # 资源ID
        self.resource_id = resource_id
        # 资源类型
        self.resource_type = resource_type
        # 标签键
        self.tag_key = tag_key
        # 标签值
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # 响应码
        self.code = code
        # 错误码
        self.error_code = error_code
        # 响应消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 请求是否成功被处理
        self.success = success
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowForWebRequest(TeaModel):
    def __init__(
        self,
        alert_conf: str = None,
        alert_ding_ding_group_biz_id: str = None,
        alert_user_group_biz_id: str = None,
        cluster_id: str = None,
        create_cluster: bool = None,
        cron_expr: str = None,
        description: str = None,
        end_schedule: int = None,
        graph: str = None,
        host_name: str = None,
        id: str = None,
        name: str = None,
        namespace: str = None,
        parent_category: str = None,
        parent_flow_list: str = None,
        periodic: bool = None,
        project_id: str = None,
        region_id: str = None,
        start_schedule: int = None,
        status: str = None,
    ):
        self.alert_conf = alert_conf
        self.alert_ding_ding_group_biz_id = alert_ding_ding_group_biz_id
        self.alert_user_group_biz_id = alert_user_group_biz_id
        self.cluster_id = cluster_id
        self.create_cluster = create_cluster
        self.cron_expr = cron_expr
        self.description = description
        self.end_schedule = end_schedule
        self.graph = graph
        self.host_name = host_name
        self.id = id
        self.name = name
        self.namespace = namespace
        self.parent_category = parent_category
        self.parent_flow_list = parent_flow_list
        self.periodic = periodic
        self.project_id = project_id
        self.region_id = region_id
        self.start_schedule = start_schedule
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.alert_ding_ding_group_biz_id is not None:
            result['AlertDingDingGroupBizId'] = self.alert_ding_ding_group_biz_id
        if self.alert_user_group_biz_id is not None:
            result['AlertUserGroupBizId'] = self.alert_user_group_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_cluster is not None:
            result['CreateCluster'] = self.create_cluster
        if self.cron_expr is not None:
            result['CronExpr'] = self.cron_expr
        if self.description is not None:
            result['Description'] = self.description
        if self.end_schedule is not None:
            result['EndSchedule'] = self.end_schedule
        if self.graph is not None:
            result['Graph'] = self.graph
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.parent_flow_list is not None:
            result['ParentFlowList'] = self.parent_flow_list
        if self.periodic is not None:
            result['Periodic'] = self.periodic
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_schedule is not None:
            result['StartSchedule'] = self.start_schedule
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('AlertDingDingGroupBizId') is not None:
            self.alert_ding_ding_group_biz_id = m.get('AlertDingDingGroupBizId')
        if m.get('AlertUserGroupBizId') is not None:
            self.alert_user_group_biz_id = m.get('AlertUserGroupBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateCluster') is not None:
            self.create_cluster = m.get('CreateCluster')
        if m.get('CronExpr') is not None:
            self.cron_expr = m.get('CronExpr')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndSchedule') is not None:
            self.end_schedule = m.get('EndSchedule')
        if m.get('Graph') is not None:
            self.graph = m.get('Graph')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ParentFlowList') is not None:
            self.parent_flow_list = m.get('ParentFlowList')
        if m.get('Periodic') is not None:
            self.periodic = m.get('Periodic')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartSchedule') is not None:
            self.start_schedule = m.get('StartSchedule')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyFlowForWebResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowForWebResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowForWebResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyFlowForWebResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowJobRequestResourceList(TeaModel):
    def __init__(
        self,
        alias: str = None,
        path: str = None,
    ):
        # 保留参数。
        self.alias = alias
        # 保留参数。
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ModifyFlowJobRequest(TeaModel):
    def __init__(
        self,
        alert_conf: str = None,
        cluster_id: str = None,
        custom_variables: str = None,
        description: str = None,
        env_conf: str = None,
        fail_act: str = None,
        id: str = None,
        knox_password: str = None,
        knox_user: str = None,
        mode: str = None,
        monitor_conf: str = None,
        name: str = None,
        param_conf: str = None,
        params: str = None,
        project_id: str = None,
        region_id: str = None,
        resource_list: List[ModifyFlowJobRequestResourceList] = None,
        retry_policy: str = None,
        run_conf: str = None,
    ):
        # 保留参数。
        self.alert_conf = alert_conf
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id
        # 自定义变量。
        self.custom_variables = custom_variables
        # 修改后的作业描述。
        self.description = description
        # 环境变量设置。
        self.env_conf = env_conf
        # 失败策略，可能的取值：CONTINUE（提过本次作业），STOP（停止作业）
        self.fail_act = fail_act
        # 需要修改的作业的ID。
        self.id = id
        # Knox的用户密码，执行Zeppelin Notebook时必须提供。
        self.knox_password = knox_password
        # Knox的用户名，执行Zeppelin Notebook时必须提供。
        self.knox_user = knox_user
        # 模型模式，取值如下：  YARN：将作业包装成一个Launcher提交至YARN中执行，LOCAL：作业直接在机器上以进程方式运行。
        self.mode = mode
        # 监控配置，仅SPARK_STREAMING类型作业支持监控配置。
        self.monitor_conf = monitor_conf
        # 修改后的作业名称。
        self.name = name
        # 参数设置。
        self.param_conf = param_conf
        # 作业内容。如果是spark作业，该参数的内容会作为spark-submit的参数。
        self.params = params
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id
        # 保留参数。
        self.resource_list = resource_list
        # 重试策略，保留参数。
        self.retry_policy = retry_policy
        # 运行配置，取值如下：priority（优先级），userName（任务的Linux提交用户），memory（内存，单位为MB），cores（核数）
        self.run_conf = run_conf

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_conf is not None:
            result['AlertConf'] = self.alert_conf
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables
        if self.description is not None:
            result['Description'] = self.description
        if self.env_conf is not None:
            result['EnvConf'] = self.env_conf
        if self.fail_act is not None:
            result['FailAct'] = self.fail_act
        if self.id is not None:
            result['Id'] = self.id
        if self.knox_password is not None:
            result['KnoxPassword'] = self.knox_password
        if self.knox_user is not None:
            result['KnoxUser'] = self.knox_user
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf
        if self.name is not None:
            result['Name'] = self.name
        if self.param_conf is not None:
            result['ParamConf'] = self.param_conf
        if self.params is not None:
            result['Params'] = self.params
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy
        if self.run_conf is not None:
            result['RunConf'] = self.run_conf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertConf') is not None:
            self.alert_conf = m.get('AlertConf')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnvConf') is not None:
            self.env_conf = m.get('EnvConf')
        if m.get('FailAct') is not None:
            self.fail_act = m.get('FailAct')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KnoxPassword') is not None:
            self.knox_password = m.get('KnoxPassword')
        if m.get('KnoxUser') is not None:
            self.knox_user = m.get('KnoxUser')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('MonitorConf') is not None:
            self.monitor_conf = m.get('MonitorConf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamConf') is not None:
            self.param_conf = m.get('ParamConf')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = ModifyFlowJobRequestResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('RetryPolicy') is not None:
            self.retry_policy = m.get('RetryPolicy')
        if m.get('RunConf') is not None:
            self.run_conf = m.get('RunConf')
        return self


class ModifyFlowJobResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # API调用结果：true（修改成功），false（修改失败）
        self.data = data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowProjectRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.description = description
        self.name = name
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyFlowProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyFlowProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseClusterRequest(TeaModel):
    def __init__(
        self,
        force_release: bool = None,
        id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.force_release = force_release
        self.id = id
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_release is not None:
            result['ForceRelease'] = self.force_release
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceRelease') is not None:
            self.force_release = m.get('ForceRelease')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseClusterResponseBody(TeaModel):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class RerunFlowRequest(TeaModel):
    def __init__(
        self,
        flow_instance_id: str = None,
        project_id: str = None,
        re_run_fail: bool = None,
        region_id: str = None,
    ):
        # 工作流实例ID。您可以调用ListFlowInstance查看工作流实例ID。
        self.flow_instance_id = flow_instance_id
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 是否只重试失败节点。
        self.re_run_fail = re_run_fail
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.re_run_fail is not None:
            result['ReRunFail'] = self.re_run_fail
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ReRunFail') is not None:
            self.re_run_fail = m.get('ReRunFail')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RerunFlowResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # 返回执行结果，包含如下：true: 重试工作流成功，false: 重试工作流失败。
        self.data = data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RerunFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RerunFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RerunFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeFlowRequest(TeaModel):
    def __init__(
        self,
        flow_instance_id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # 工作流实例ID。您可以调用ListFlowInstance查看工作流ID。
        self.flow_instance_id = flow_instance_id
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 区域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_instance_id is not None:
            result['FlowInstanceId'] = self.flow_instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowInstanceId') is not None:
            self.flow_instance_id = m.get('FlowInstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResumeFlowResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        # 返回执行结果。
        self.data = data
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResumeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ResumeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFlowRequest(TeaModel):
    def __init__(
        self,
        conf: str = None,
        flow_id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # 配置信息{"key":"value"}格式。  本示例中cyctime表示实际调度运行的时间（长整型时间戳）。
        self.conf = conf
        # 工作流ID。您可以调用ListFlowInstance查看工作流ID。
        self.flow_id = flow_id
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitFlowResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        id: str = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # 过期参数。
        self.data = data
        # 工作流实例ID。
        self.id = id
        # 过期参数。
        self.instance_id = instance_id
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitFlowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitFlowJobRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        conf: str = None,
        host_name: str = None,
        job_id: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # 集群ID。您可以调用ListClusters查看集群的ID。
        self.cluster_id = cluster_id
        # 配置参数信息：{"key1":"value1"}。key为params的参数值会覆盖实际作业中运行的内容。
        self.conf = conf
        # 保留参数。
        self.host_name = host_name
        # 作业ID。您可以调用ListFlowJob查看作业ID。
        self.job_id = job_id
        # 项目ID。您可以调用ListFlowProject查看项目的ID。
        self.project_id = project_id
        # 地域ID。您可以调用DescribeRegions查看最新的阿里云地域列表。
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
        if self.conf is not None:
            result['Conf'] = self.conf
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Conf') is not None:
            self.conf = m.get('Conf')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SubmitFlowJobResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # 运行的作业实例ID。
        self.id = id
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SubmitFlowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # 资源ID
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # 资源类型
        self.resource_type = resource_type
        # 标签列表
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 错误码
        self.error_code = error_code
        # 响应消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 请求是否成功被处理
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallLibrariesRequest(TeaModel):
    def __init__(
        self,
        cluster_biz_id_list: List[str] = None,
        library_biz_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        self.cluster_biz_id_list = cluster_biz_id_list
        self.library_biz_id = library_biz_id
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id_list is not None:
            result['ClusterBizIdList'] = self.cluster_biz_id_list
        if self.library_biz_id is not None:
            result['LibraryBizId'] = self.library_biz_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizIdList') is not None:
            self.cluster_biz_id_list = m.get('ClusterBizIdList')
        if m.get('LibraryBizId') is not None:
            self.library_biz_id = m.get('LibraryBizId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UninstallLibrariesResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UninstallLibrariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallLibrariesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UninstallLibrariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # 是否解绑资源的所有标签
        self.all = all
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # 集群ID列表
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # 资源类型
        self.resource_type = resource_type
        # 解绑的标签键列表
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 响应码
        self.code = code
        # 错误码
        self.error_code = error_code
        # 响应消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 请求是否成功被处理
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLibraryInstallTaskStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_biz_id: str = None,
    ):
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.status = status
        self.task_biz_id = task_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_biz_id is not None:
            result['TaskBizId'] = self.task_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskBizId') is not None:
            self.task_biz_id = m.get('TaskBizId')
        return self


class UpdateLibraryInstallTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLibraryInstallTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLibraryInstallTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateLibraryInstallTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


