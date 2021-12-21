# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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
        body: CreateClusterV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateClusterV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowJobRequestResourceList(TeaModel):
    def __init__(
        self,
        alias: str = None,
        path: str = None,
    ):
        self.alias = alias
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
        self.adhoc = adhoc
        self.alert_conf = alert_conf
        self.client_token = client_token
        self.cluster_id = cluster_id
        self.custom_variables = custom_variables
        self.description = description
        self.env_conf = env_conf
        self.fail_act = fail_act
        self.mode = mode
        self.monitor_conf = monitor_conf
        self.name = name
        self.param_conf = param_conf
        self.params = params
        self.parent_category = parent_category
        self.project_id = project_id
        self.region_id = region_id
        self.resource_list = resource_list
        self.retry_policy = retry_policy
        self.run_conf = run_conf
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


class CreateFlowJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlowJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.description = description
        self.name = name
        self.product_type = product_type
        self.region_id = region_id
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


class CreateFlowProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlowProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowProjectResponseBody()
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
        body: DescribeClusterV2ResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClusterV2ResponseBody()
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
        body: ListClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMainVersionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
    ):
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id

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
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList(TeaModel):
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


class ListMainVersionsResponseBodyMainVersionList(TeaModel):
    def __init__(
        self,
        cluster_type_info_list: List[ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList] = None,
        extra_info: str = None,
        main_version_name: str = None,
        region_id: str = None,
    ):
        self.cluster_type_info_list = cluster_type_info_list
        self.extra_info = extra_info
        self.main_version_name = main_version_name
        self.region_id = region_id

    def validate(self):
        if self.cluster_type_info_list:
            for k in self.cluster_type_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterTypeInfoList'] = []
        if self.cluster_type_info_list is not None:
            for k in self.cluster_type_info_list:
                result['ClusterTypeInfoList'].append(k.to_map() if k else None)
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.main_version_name is not None:
            result['MainVersionName'] = self.main_version_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_type_info_list = []
        if m.get('ClusterTypeInfoList') is not None:
            for k in m.get('ClusterTypeInfoList'):
                temp_model = ListMainVersionsResponseBodyMainVersionListClusterTypeInfoList()
                self.cluster_type_info_list.append(temp_model.from_map(k))
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('MainVersionName') is not None:
            self.main_version_name = m.get('MainVersionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListMainVersionsResponseBody(TeaModel):
    def __init__(
        self,
        main_version_list: List[ListMainVersionsResponseBodyMainVersionList] = None,
        request_id: str = None,
    ):
        self.main_version_list = main_version_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.main_version_list:
            for k in self.main_version_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MainVersionList'] = []
        if self.main_version_list is not None:
            for k in self.main_version_list:
                result['MainVersionList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.main_version_list = []
        if m.get('MainVersionList') is not None:
            for k in m.get('MainVersionList'):
                temp_model = ListMainVersionsResponseBodyMainVersionList()
                self.main_version_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMainVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMainVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMainVersionsResponseBody()
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
        body: ReleaseClusterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


