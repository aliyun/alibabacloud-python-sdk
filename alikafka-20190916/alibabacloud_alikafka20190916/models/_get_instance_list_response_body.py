# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        instance_list: main_models.GetInstanceListResponseBodyInstanceList = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the call is successful.
        self.code = code
        self.instance_list = instance_list
        # The message returned.
        self.message = message
        # The ID of the region.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()

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

        if m.get('InstanceList') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m.get('InstanceList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceListResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        instance_vo: List[main_models.GetInstanceListResponseBodyInstanceListInstanceVO] = None,
    ):
        self.instance_vo = instance_vo

    def validate(self):
        if self.instance_vo:
            for v1 in self.instance_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceVO'] = []
        if self.instance_vo is not None:
            for k1 in self.instance_vo:
                result['InstanceVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_vo = []
        if m.get('InstanceVO') is not None:
            for k1 in m.get('InstanceVO'):
                temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVO()
                self.instance_vo.append(temp_model.from_map(k1))

        return self

class GetInstanceListResponseBodyInstanceListInstanceVO(DaraModel):
    def __init__(
        self,
        all_config: str = None,
        auto_create_group_enable: bool = None,
        auto_create_topic_enable: bool = None,
        backup_zone_id: str = None,
        confluent_config: main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfig = None,
        confluent_instance_components: main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentInstanceComponents = None,
        create_time: int = None,
        default_partition_num: int = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: int = None,
        domain_endpoint: str = None,
        eip_max: int = None,
        end_point: str = None,
        expired_time: int = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_read: int = None,
        io_max_spec: str = None,
        io_max_write: int = None,
        kms_key_id: str = None,
        msg_retain: int = None,
        name: str = None,
        paid_type: int = None,
        recommended_partition_count: int = None,
        region_id: str = None,
        reserved_publish_capacity: int = None,
        reserved_subscribe_capacity: int = None,
        resource_group_id: str = None,
        sasl_domain_endpoint: str = None,
        sasl_end_point: str = None,
        scheduled_retirement: bool = None,
        security_group: str = None,
        series: str = None,
        service_status: int = None,
        spec_type: str = None,
        ssl_domain_endpoint: str = None,
        ssl_end_point: str = None,
        standard_zone_id: str = None,
        tags: main_models.GetInstanceListResponseBodyInstanceListInstanceVOTags = None,
        topic_num_limit: int = None,
        upgrade_service_detail_info: main_models.GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo = None,
        used_group_count: int = None,
        used_partition_count: int = None,
        used_topic_count: int = None,
        v_switch_id: str = None,
        v_switch_ids: main_models.GetInstanceListResponseBodyInstanceListInstanceVOVSwitchIds = None,
        view_instance_status_code: int = None,
        vpc_id: str = None,
        vpc_sasl_domain_endpoint: str = None,
        vpc_sasl_end_point: str = None,
        zone_id: str = None,
    ):
        self.all_config = all_config
        self.auto_create_group_enable = auto_create_group_enable
        self.auto_create_topic_enable = auto_create_topic_enable
        self.backup_zone_id = backup_zone_id
        self.confluent_config = confluent_config
        self.confluent_instance_components = confluent_instance_components
        self.create_time = create_time
        self.default_partition_num = default_partition_num
        self.deploy_type = deploy_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.domain_endpoint = domain_endpoint
        self.eip_max = eip_max
        self.end_point = end_point
        self.expired_time = expired_time
        self.instance_id = instance_id
        self.io_max = io_max
        self.io_max_read = io_max_read
        self.io_max_spec = io_max_spec
        self.io_max_write = io_max_write
        self.kms_key_id = kms_key_id
        self.msg_retain = msg_retain
        self.name = name
        self.paid_type = paid_type
        self.recommended_partition_count = recommended_partition_count
        self.region_id = region_id
        self.reserved_publish_capacity = reserved_publish_capacity
        self.reserved_subscribe_capacity = reserved_subscribe_capacity
        self.resource_group_id = resource_group_id
        self.sasl_domain_endpoint = sasl_domain_endpoint
        self.sasl_end_point = sasl_end_point
        self.scheduled_retirement = scheduled_retirement
        self.security_group = security_group
        self.series = series
        self.service_status = service_status
        self.spec_type = spec_type
        self.ssl_domain_endpoint = ssl_domain_endpoint
        self.ssl_end_point = ssl_end_point
        self.standard_zone_id = standard_zone_id
        self.tags = tags
        self.topic_num_limit = topic_num_limit
        self.upgrade_service_detail_info = upgrade_service_detail_info
        self.used_group_count = used_group_count
        self.used_partition_count = used_partition_count
        self.used_topic_count = used_topic_count
        self.v_switch_id = v_switch_id
        self.v_switch_ids = v_switch_ids
        self.view_instance_status_code = view_instance_status_code
        self.vpc_id = vpc_id
        self.vpc_sasl_domain_endpoint = vpc_sasl_domain_endpoint
        self.vpc_sasl_end_point = vpc_sasl_end_point
        self.zone_id = zone_id

    def validate(self):
        if self.confluent_config:
            self.confluent_config.validate()
        if self.confluent_instance_components:
            self.confluent_instance_components.validate()
        if self.tags:
            self.tags.validate()
        if self.upgrade_service_detail_info:
            self.upgrade_service_detail_info.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_config is not None:
            result['AllConfig'] = self.all_config

        if self.auto_create_group_enable is not None:
            result['AutoCreateGroupEnable'] = self.auto_create_group_enable

        if self.auto_create_topic_enable is not None:
            result['AutoCreateTopicEnable'] = self.auto_create_topic_enable

        if self.backup_zone_id is not None:
            result['BackupZoneId'] = self.backup_zone_id

        if self.confluent_config is not None:
            result['ConfluentConfig'] = self.confluent_config.to_map()

        if self.confluent_instance_components is not None:
            result['ConfluentInstanceComponents'] = self.confluent_instance_components.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_partition_num is not None:
            result['DefaultPartitionNum'] = self.default_partition_num

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.domain_endpoint is not None:
            result['DomainEndpoint'] = self.domain_endpoint

        if self.eip_max is not None:
            result['EipMax'] = self.eip_max

        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.io_max is not None:
            result['IoMax'] = self.io_max

        if self.io_max_read is not None:
            result['IoMaxRead'] = self.io_max_read

        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec

        if self.io_max_write is not None:
            result['IoMaxWrite'] = self.io_max_write

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.msg_retain is not None:
            result['MsgRetain'] = self.msg_retain

        if self.name is not None:
            result['Name'] = self.name

        if self.paid_type is not None:
            result['PaidType'] = self.paid_type

        if self.recommended_partition_count is not None:
            result['RecommendedPartitionCount'] = self.recommended_partition_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_publish_capacity is not None:
            result['ReservedPublishCapacity'] = self.reserved_publish_capacity

        if self.reserved_subscribe_capacity is not None:
            result['ReservedSubscribeCapacity'] = self.reserved_subscribe_capacity

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sasl_domain_endpoint is not None:
            result['SaslDomainEndpoint'] = self.sasl_domain_endpoint

        if self.sasl_end_point is not None:
            result['SaslEndPoint'] = self.sasl_end_point

        if self.scheduled_retirement is not None:
            result['ScheduledRetirement'] = self.scheduled_retirement

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.series is not None:
            result['Series'] = self.series

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.ssl_domain_endpoint is not None:
            result['SslDomainEndpoint'] = self.ssl_domain_endpoint

        if self.ssl_end_point is not None:
            result['SslEndPoint'] = self.ssl_end_point

        if self.standard_zone_id is not None:
            result['StandardZoneId'] = self.standard_zone_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.topic_num_limit is not None:
            result['TopicNumLimit'] = self.topic_num_limit

        if self.upgrade_service_detail_info is not None:
            result['UpgradeServiceDetailInfo'] = self.upgrade_service_detail_info.to_map()

        if self.used_group_count is not None:
            result['UsedGroupCount'] = self.used_group_count

        if self.used_partition_count is not None:
            result['UsedPartitionCount'] = self.used_partition_count

        if self.used_topic_count is not None:
            result['UsedTopicCount'] = self.used_topic_count

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.view_instance_status_code is not None:
            result['ViewInstanceStatusCode'] = self.view_instance_status_code

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_sasl_domain_endpoint is not None:
            result['VpcSaslDomainEndpoint'] = self.vpc_sasl_domain_endpoint

        if self.vpc_sasl_end_point is not None:
            result['VpcSaslEndPoint'] = self.vpc_sasl_end_point

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllConfig') is not None:
            self.all_config = m.get('AllConfig')

        if m.get('AutoCreateGroupEnable') is not None:
            self.auto_create_group_enable = m.get('AutoCreateGroupEnable')

        if m.get('AutoCreateTopicEnable') is not None:
            self.auto_create_topic_enable = m.get('AutoCreateTopicEnable')

        if m.get('BackupZoneId') is not None:
            self.backup_zone_id = m.get('BackupZoneId')

        if m.get('ConfluentConfig') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfig()
            self.confluent_config = temp_model.from_map(m.get('ConfluentConfig'))

        if m.get('ConfluentInstanceComponents') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentInstanceComponents()
            self.confluent_instance_components = temp_model.from_map(m.get('ConfluentInstanceComponents'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultPartitionNum') is not None:
            self.default_partition_num = m.get('DefaultPartitionNum')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('DomainEndpoint') is not None:
            self.domain_endpoint = m.get('DomainEndpoint')

        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')

        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')

        if m.get('IoMaxRead') is not None:
            self.io_max_read = m.get('IoMaxRead')

        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')

        if m.get('IoMaxWrite') is not None:
            self.io_max_write = m.get('IoMaxWrite')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MsgRetain') is not None:
            self.msg_retain = m.get('MsgRetain')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')

        if m.get('RecommendedPartitionCount') is not None:
            self.recommended_partition_count = m.get('RecommendedPartitionCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedPublishCapacity') is not None:
            self.reserved_publish_capacity = m.get('ReservedPublishCapacity')

        if m.get('ReservedSubscribeCapacity') is not None:
            self.reserved_subscribe_capacity = m.get('ReservedSubscribeCapacity')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SaslDomainEndpoint') is not None:
            self.sasl_domain_endpoint = m.get('SaslDomainEndpoint')

        if m.get('SaslEndPoint') is not None:
            self.sasl_end_point = m.get('SaslEndPoint')

        if m.get('ScheduledRetirement') is not None:
            self.scheduled_retirement = m.get('ScheduledRetirement')

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('SslDomainEndpoint') is not None:
            self.ssl_domain_endpoint = m.get('SslDomainEndpoint')

        if m.get('SslEndPoint') is not None:
            self.ssl_end_point = m.get('SslEndPoint')

        if m.get('StandardZoneId') is not None:
            self.standard_zone_id = m.get('StandardZoneId')

        if m.get('Tags') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TopicNumLimit') is not None:
            self.topic_num_limit = m.get('TopicNumLimit')

        if m.get('UpgradeServiceDetailInfo') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo()
            self.upgrade_service_detail_info = temp_model.from_map(m.get('UpgradeServiceDetailInfo'))

        if m.get('UsedGroupCount') is not None:
            self.used_group_count = m.get('UsedGroupCount')

        if m.get('UsedPartitionCount') is not None:
            self.used_partition_count = m.get('UsedPartitionCount')

        if m.get('UsedTopicCount') is not None:
            self.used_topic_count = m.get('UsedTopicCount')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('ViewInstanceStatusCode') is not None:
            self.view_instance_status_code = m.get('ViewInstanceStatusCode')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcSaslDomainEndpoint') is not None:
            self.vpc_sasl_domain_endpoint = m.get('VpcSaslDomainEndpoint')

        if m.get('VpcSaslEndPoint') is not None:
            self.vpc_sasl_end_point = m.get('VpcSaslEndPoint')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_ids: List[str] = None,
    ):
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOUpgradeServiceDetailInfo(DaraModel):
    def __init__(
        self,
        current_2open_source_version: str = None,
    ):
        self.current_2open_source_version = current_2open_source_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_2open_source_version is not None:
            result['Current2OpenSourceVersion'] = self.current_2open_source_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current2OpenSourceVersion') is not None:
            self.current_2open_source_version = m.get('Current2OpenSourceVersion')

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOTags(DaraModel):
    def __init__(
        self,
        tag_vo: List[main_models.GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO] = None,
    ):
        self.tag_vo = tag_vo

    def validate(self):
        if self.tag_vo:
            for v1 in self.tag_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k1 in self.tag_vo:
                result['TagVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k1 in m.get('TagVO'):
                temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k1))

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOTagsTagVO(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetInstanceListResponseBodyInstanceListInstanceVOConfluentInstanceComponents(DaraModel):
    def __init__(
        self,
        confluent_instance_component_vo: List[main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentInstanceComponentsConfluentInstanceComponentVO] = None,
    ):
        self.confluent_instance_component_vo = confluent_instance_component_vo

    def validate(self):
        if self.confluent_instance_component_vo:
            for v1 in self.confluent_instance_component_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfluentInstanceComponentVO'] = []
        if self.confluent_instance_component_vo is not None:
            for k1 in self.confluent_instance_component_vo:
                result['ConfluentInstanceComponentVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.confluent_instance_component_vo = []
        if m.get('ConfluentInstanceComponentVO') is not None:
            for k1 in m.get('ConfluentInstanceComponentVO'):
                temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentInstanceComponentsConfluentInstanceComponentVO()
                self.confluent_instance_component_vo.append(temp_model.from_map(k1))

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOConfluentInstanceComponentsConfluentInstanceComponentVO(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        deploy_module: str = None,
        pub_endpoint: str = None,
        vpc_endpoint: str = None,
        internal_id: str = None,
    ):
        self.component_type = component_type
        self.deploy_module = deploy_module
        self.pub_endpoint = pub_endpoint
        self.vpc_endpoint = vpc_endpoint
        self.internal_id = internal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.deploy_module is not None:
            result['DeployModule'] = self.deploy_module

        if self.pub_endpoint is not None:
            result['PubEndpoint'] = self.pub_endpoint

        if self.vpc_endpoint is not None:
            result['VpcEndpoint'] = self.vpc_endpoint

        if self.internal_id is not None:
            result['internalId'] = self.internal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('DeployModule') is not None:
            self.deploy_module = m.get('DeployModule')

        if m.get('PubEndpoint') is not None:
            self.pub_endpoint = m.get('PubEndpoint')

        if m.get('VpcEndpoint') is not None:
            self.vpc_endpoint = m.get('VpcEndpoint')

        if m.get('internalId') is not None:
            self.internal_id = m.get('internalId')

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfig(DaraModel):
    def __init__(
        self,
        connect_cu: int = None,
        connect_replica: int = None,
        control_center_cu: int = None,
        control_center_replica: int = None,
        control_center_storage: int = None,
        kafka_cu: int = None,
        kafka_replica: int = None,
        kafka_rest_proxy_cu: int = None,
        kafka_rest_proxy_replica: int = None,
        kafka_storage: int = None,
        ksql_cu: int = None,
        ksql_list: main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfigKsqlList = None,
        ksql_replica: int = None,
        ksql_storage: int = None,
        schema_registry_cu: int = None,
        schema_registry_replica: int = None,
        zoo_keeper_cu: int = None,
        zoo_keeper_replica: int = None,
        zoo_keeper_storage: int = None,
    ):
        self.connect_cu = connect_cu
        self.connect_replica = connect_replica
        self.control_center_cu = control_center_cu
        self.control_center_replica = control_center_replica
        self.control_center_storage = control_center_storage
        self.kafka_cu = kafka_cu
        self.kafka_replica = kafka_replica
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        self.kafka_storage = kafka_storage
        self.ksql_cu = ksql_cu
        self.ksql_list = ksql_list
        self.ksql_replica = ksql_replica
        self.ksql_storage = ksql_storage
        self.schema_registry_cu = schema_registry_cu
        self.schema_registry_replica = schema_registry_replica
        self.zoo_keeper_cu = zoo_keeper_cu
        self.zoo_keeper_replica = zoo_keeper_replica
        self.zoo_keeper_storage = zoo_keeper_storage

    def validate(self):
        if self.ksql_list:
            self.ksql_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_cu is not None:
            result['ConnectCU'] = self.connect_cu

        if self.connect_replica is not None:
            result['ConnectReplica'] = self.connect_replica

        if self.control_center_cu is not None:
            result['ControlCenterCU'] = self.control_center_cu

        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica

        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage

        if self.kafka_cu is not None:
            result['KafkaCU'] = self.kafka_cu

        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica

        if self.kafka_rest_proxy_cu is not None:
            result['KafkaRestProxyCU'] = self.kafka_rest_proxy_cu

        if self.kafka_rest_proxy_replica is not None:
            result['KafkaRestProxyReplica'] = self.kafka_rest_proxy_replica

        if self.kafka_storage is not None:
            result['KafkaStorage'] = self.kafka_storage

        if self.ksql_cu is not None:
            result['KsqlCU'] = self.ksql_cu

        if self.ksql_list is not None:
            result['KsqlList'] = self.ksql_list.to_map()

        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica

        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage

        if self.schema_registry_cu is not None:
            result['SchemaRegistryCU'] = self.schema_registry_cu

        if self.schema_registry_replica is not None:
            result['SchemaRegistryReplica'] = self.schema_registry_replica

        if self.zoo_keeper_cu is not None:
            result['ZooKeeperCU'] = self.zoo_keeper_cu

        if self.zoo_keeper_replica is not None:
            result['ZooKeeperReplica'] = self.zoo_keeper_replica

        if self.zoo_keeper_storage is not None:
            result['ZooKeeperStorage'] = self.zoo_keeper_storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectCU') is not None:
            self.connect_cu = m.get('ConnectCU')

        if m.get('ConnectReplica') is not None:
            self.connect_replica = m.get('ConnectReplica')

        if m.get('ControlCenterCU') is not None:
            self.control_center_cu = m.get('ControlCenterCU')

        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')

        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')

        if m.get('KafkaCU') is not None:
            self.kafka_cu = m.get('KafkaCU')

        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')

        if m.get('KafkaRestProxyCU') is not None:
            self.kafka_rest_proxy_cu = m.get('KafkaRestProxyCU')

        if m.get('KafkaRestProxyReplica') is not None:
            self.kafka_rest_proxy_replica = m.get('KafkaRestProxyReplica')

        if m.get('KafkaStorage') is not None:
            self.kafka_storage = m.get('KafkaStorage')

        if m.get('KsqlCU') is not None:
            self.ksql_cu = m.get('KsqlCU')

        if m.get('KsqlList') is not None:
            temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfigKsqlList()
            self.ksql_list = temp_model.from_map(m.get('KsqlList'))

        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')

        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')

        if m.get('SchemaRegistryCU') is not None:
            self.schema_registry_cu = m.get('SchemaRegistryCU')

        if m.get('SchemaRegistryReplica') is not None:
            self.schema_registry_replica = m.get('SchemaRegistryReplica')

        if m.get('ZooKeeperCU') is not None:
            self.zoo_keeper_cu = m.get('ZooKeeperCU')

        if m.get('ZooKeeperReplica') is not None:
            self.zoo_keeper_replica = m.get('ZooKeeperReplica')

        if m.get('ZooKeeperStorage') is not None:
            self.zoo_keeper_storage = m.get('ZooKeeperStorage')

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfigKsqlList(DaraModel):
    def __init__(
        self,
        confluent_instance_component_resource_vo: List[main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfigKsqlListConfluentInstanceComponentResourceVO] = None,
    ):
        self.confluent_instance_component_resource_vo = confluent_instance_component_resource_vo

    def validate(self):
        if self.confluent_instance_component_resource_vo:
            for v1 in self.confluent_instance_component_resource_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfluentInstanceComponentResourceVO'] = []
        if self.confluent_instance_component_resource_vo is not None:
            for k1 in self.confluent_instance_component_resource_vo:
                result['ConfluentInstanceComponentResourceVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.confluent_instance_component_resource_vo = []
        if m.get('ConfluentInstanceComponentResourceVO') is not None:
            for k1 in m.get('ConfluentInstanceComponentResourceVO'):
                temp_model = main_models.GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfigKsqlListConfluentInstanceComponentResourceVO()
                self.confluent_instance_component_resource_vo.append(temp_model.from_map(k1))

        return self

class GetInstanceListResponseBodyInstanceListInstanceVOConfluentConfigKsqlListConfluentInstanceComponentResourceVO(DaraModel):
    def __init__(
        self,
        cu: int = None,
        internal_id: str = None,
        replica: int = None,
        storage: int = None,
        type: str = None,
    ):
        self.cu = cu
        self.internal_id = internal_id
        self.replica = replica
        self.storage = storage
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.internal_id is not None:
            result['InternalId'] = self.internal_id

        if self.replica is not None:
            result['Replica'] = self.replica

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('InternalId') is not None:
            self.internal_id = m.get('InternalId')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

