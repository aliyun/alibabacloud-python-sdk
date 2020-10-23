# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class GetResourceComplianceTimelineRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, start_time=None, end_time=None, limit=None,
                 multi_account=None, member_id=None, region=None, next_token=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.limit = limit              # type: int
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: str
        self.region = region            # type: str
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Limit'] = self.limit
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        result['Region'] = self.region
        result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.limit = map.get('Limit')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        self.region = map.get('Region')
        self.next_token = map.get('NextToken')
        return self


class GetResourceComplianceTimelineResponse(TeaModel):
    def __init__(self, request_id=None, resource_compliance_timeline=None):
        self.request_id = request_id    # type: str
        self.resource_compliance_timeline = resource_compliance_timeline  # type: GetResourceComplianceTimelineResponseResourceComplianceTimeline

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_compliance_timeline, 'resource_compliance_timeline')
        if self.resource_compliance_timeline:
            self.resource_compliance_timeline.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.resource_compliance_timeline is not None:
            result['ResourceComplianceTimeline'] = self.resource_compliance_timeline.to_map()
        else:
            result['ResourceComplianceTimeline'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ResourceComplianceTimeline') is not None:
            temp_model = GetResourceComplianceTimelineResponseResourceComplianceTimeline()
            self.resource_compliance_timeline = temp_model.from_map(map['ResourceComplianceTimeline'])
        else:
            self.resource_compliance_timeline = None
        return self


class GetResourceComplianceTimelineResponseResourceComplianceTimelineComplianceList(TeaModel):
    def __init__(self, account_id=None, availability_zone=None, capture_time=None, configuration=None,
                 configuration_diff=None, region=None, resource_create_time=None, resource_id=None, resource_name=None,
                 resource_status=None, resource_type=None, tags=None):
        self.account_id = account_id    # type: str
        self.availability_zone = availability_zone  # type: str
        self.capture_time = capture_time  # type: int
        self.configuration = configuration  # type: str
        self.configuration_diff = configuration_diff  # type: str
        self.region = region            # type: str
        self.resource_create_time = resource_create_time  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_status = resource_status  # type: str
        self.resource_type = resource_type  # type: str
        self.tags = tags                # type: str

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.availability_zone, 'availability_zone')
        self.validate_required(self.capture_time, 'capture_time')
        self.validate_required(self.configuration, 'configuration')
        self.validate_required(self.configuration_diff, 'configuration_diff')
        self.validate_required(self.region, 'region')
        self.validate_required(self.resource_create_time, 'resource_create_time')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.resource_status, 'resource_status')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tags, 'tags')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['AvailabilityZone'] = self.availability_zone
        result['CaptureTime'] = self.capture_time
        result['Configuration'] = self.configuration
        result['ConfigurationDiff'] = self.configuration_diff
        result['Region'] = self.region
        result['ResourceCreateTime'] = self.resource_create_time
        result['ResourceId'] = self.resource_id
        result['ResourceName'] = self.resource_name
        result['ResourceStatus'] = self.resource_status
        result['ResourceType'] = self.resource_type
        result['Tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.availability_zone = map.get('AvailabilityZone')
        self.capture_time = map.get('CaptureTime')
        self.configuration = map.get('Configuration')
        self.configuration_diff = map.get('ConfigurationDiff')
        self.region = map.get('Region')
        self.resource_create_time = map.get('ResourceCreateTime')
        self.resource_id = map.get('ResourceId')
        self.resource_name = map.get('ResourceName')
        self.resource_status = map.get('ResourceStatus')
        self.resource_type = map.get('ResourceType')
        self.tags = map.get('Tags')
        return self


class GetResourceComplianceTimelineResponseResourceComplianceTimeline(TeaModel):
    def __init__(self, limit=None, total_count=None, next_token=None, compliance_list=None):
        self.limit = limit              # type: int
        self.total_count = total_count  # type: int
        self.next_token = next_token    # type: str
        self.compliance_list = compliance_list  # type: List[GetResourceComplianceTimelineResponseResourceComplianceTimelineComplianceList]

    def validate(self):
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.compliance_list, 'compliance_list')
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Limit'] = self.limit
        result['TotalCount'] = self.total_count
        result['NextToken'] = self.next_token
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        else:
            result['ComplianceList'] = None
        return result

    def from_map(self, map={}):
        self.limit = map.get('Limit')
        self.total_count = map.get('TotalCount')
        self.next_token = map.get('NextToken')
        self.compliance_list = []
        if map.get('ComplianceList') is not None:
            for k in map.get('ComplianceList'):
                temp_model = GetResourceComplianceTimelineResponseResourceComplianceTimelineComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        else:
            self.compliance_list = None
        return self


class GetResourceConfigurationTimelineRequest(TeaModel):
    def __init__(self, resource_id=None, start_time=None, end_time=None, limit=None, resource_type=None, region=None,
                 multi_account=None, member_id=None, next_token=None):
        self.resource_id = resource_id  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.limit = limit              # type: int
        self.resource_type = resource_type  # type: str
        self.region = region            # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Limit'] = self.limit
        result['ResourceType'] = self.resource_type
        result['Region'] = self.region
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.limit = map.get('Limit')
        self.resource_type = map.get('ResourceType')
        self.region = map.get('Region')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        self.next_token = map.get('NextToken')
        return self


class GetResourceConfigurationTimelineResponse(TeaModel):
    def __init__(self, request_id=None, resource_configuration_timeline=None):
        self.request_id = request_id    # type: str
        self.resource_configuration_timeline = resource_configuration_timeline  # type: GetResourceConfigurationTimelineResponseResourceConfigurationTimeline

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_configuration_timeline, 'resource_configuration_timeline')
        if self.resource_configuration_timeline:
            self.resource_configuration_timeline.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.resource_configuration_timeline is not None:
            result['ResourceConfigurationTimeline'] = self.resource_configuration_timeline.to_map()
        else:
            result['ResourceConfigurationTimeline'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ResourceConfigurationTimeline') is not None:
            temp_model = GetResourceConfigurationTimelineResponseResourceConfigurationTimeline()
            self.resource_configuration_timeline = temp_model.from_map(map['ResourceConfigurationTimeline'])
        else:
            self.resource_configuration_timeline = None
        return self


class GetResourceConfigurationTimelineResponseResourceConfigurationTimelineConfigurationList(TeaModel):
    def __init__(self, account_id=None, availability_zone=None, capture_time=None, configuration_diff=None,
                 region=None, relationship=None, relationship_diff=None, resource_create_time=None, resource_id=None,
                 resource_name=None, resource_type=None, tags=None):
        self.account_id = account_id    # type: int
        self.availability_zone = availability_zone  # type: str
        self.capture_time = capture_time  # type: str
        self.configuration_diff = configuration_diff  # type: str
        self.region = region            # type: str
        self.relationship = relationship  # type: str
        self.relationship_diff = relationship_diff  # type: str
        self.resource_create_time = resource_create_time  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.tags = tags                # type: str

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.availability_zone, 'availability_zone')
        self.validate_required(self.capture_time, 'capture_time')
        self.validate_required(self.configuration_diff, 'configuration_diff')
        self.validate_required(self.region, 'region')
        self.validate_required(self.relationship, 'relationship')
        self.validate_required(self.relationship_diff, 'relationship_diff')
        self.validate_required(self.resource_create_time, 'resource_create_time')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tags, 'tags')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['AvailabilityZone'] = self.availability_zone
        result['CaptureTime'] = self.capture_time
        result['ConfigurationDiff'] = self.configuration_diff
        result['Region'] = self.region
        result['Relationship'] = self.relationship
        result['RelationshipDiff'] = self.relationship_diff
        result['ResourceCreateTime'] = self.resource_create_time
        result['ResourceId'] = self.resource_id
        result['ResourceName'] = self.resource_name
        result['ResourceType'] = self.resource_type
        result['Tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.availability_zone = map.get('AvailabilityZone')
        self.capture_time = map.get('CaptureTime')
        self.configuration_diff = map.get('ConfigurationDiff')
        self.region = map.get('Region')
        self.relationship = map.get('Relationship')
        self.relationship_diff = map.get('RelationshipDiff')
        self.resource_create_time = map.get('ResourceCreateTime')
        self.resource_id = map.get('ResourceId')
        self.resource_name = map.get('ResourceName')
        self.resource_type = map.get('ResourceType')
        self.tags = map.get('Tags')
        return self


class GetResourceConfigurationTimelineResponseResourceConfigurationTimeline(TeaModel):
    def __init__(self, next_token=None, limit=None, total_count=None, configuration_list=None):
        self.next_token = next_token    # type: str
        self.limit = limit              # type: int
        self.total_count = total_count  # type: int
        self.configuration_list = configuration_list  # type: List[GetResourceConfigurationTimelineResponseResourceConfigurationTimelineConfigurationList]

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.configuration_list, 'configuration_list')
        if self.configuration_list:
            for k in self.configuration_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['Limit'] = self.limit
        result['TotalCount'] = self.total_count
        result['ConfigurationList'] = []
        if self.configuration_list is not None:
            for k in self.configuration_list:
                result['ConfigurationList'].append(k.to_map() if k else None)
        else:
            result['ConfigurationList'] = None
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.limit = map.get('Limit')
        self.total_count = map.get('TotalCount')
        self.configuration_list = []
        if map.get('ConfigurationList') is not None:
            for k in map.get('ConfigurationList'):
                temp_model = GetResourceConfigurationTimelineResponseResourceConfigurationTimelineConfigurationList()
                self.configuration_list.append(temp_model.from_map(k))
        else:
            self.configuration_list = None
        return self


class DescribeDeliveryChannelsRequest(TeaModel):
    def __init__(self, delivery_channel_ids=None):
        self.delivery_channel_ids = delivery_channel_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DeliveryChannelIds'] = self.delivery_channel_ids
        return result

    def from_map(self, map={}):
        self.delivery_channel_ids = map.get('DeliveryChannelIds')
        return self


class DescribeDeliveryChannelsResponse(TeaModel):
    def __init__(self, request_id=None, delivery_channels=None):
        self.request_id = request_id    # type: str
        self.delivery_channels = delivery_channels  # type: List[DescribeDeliveryChannelsResponseDeliveryChannels]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.delivery_channels, 'delivery_channels')
        if self.delivery_channels:
            for k in self.delivery_channels:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k in self.delivery_channels:
                result['DeliveryChannels'].append(k.to_map() if k else None)
        else:
            result['DeliveryChannels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.delivery_channels = []
        if map.get('DeliveryChannels') is not None:
            for k in map.get('DeliveryChannels'):
                temp_model = DescribeDeliveryChannelsResponseDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k))
        else:
            self.delivery_channels = None
        return self


class DescribeDeliveryChannelsResponseDeliveryChannels(TeaModel):
    def __init__(self, delivery_channel_id=None, delivery_channel_name=None, delivery_channel_type=None,
                 delivery_channel_target_arn=None, delivery_channel_assume_role_arn=None, delivery_channel_condition=None, description=None,
                 status=None):
        self.delivery_channel_id = delivery_channel_id  # type: str
        self.delivery_channel_name = delivery_channel_name  # type: str
        self.delivery_channel_type = delivery_channel_type  # type: str
        self.delivery_channel_target_arn = delivery_channel_target_arn  # type: str
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn  # type: str
        self.delivery_channel_condition = delivery_channel_condition  # type: str
        self.description = description  # type: str
        self.status = status            # type: int

    def validate(self):
        self.validate_required(self.delivery_channel_id, 'delivery_channel_id')
        self.validate_required(self.delivery_channel_name, 'delivery_channel_name')
        self.validate_required(self.delivery_channel_type, 'delivery_channel_type')
        self.validate_required(self.delivery_channel_target_arn, 'delivery_channel_target_arn')
        self.validate_required(self.delivery_channel_assume_role_arn, 'delivery_channel_assume_role_arn')
        self.validate_required(self.delivery_channel_condition, 'delivery_channel_condition')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['DeliveryChannelId'] = self.delivery_channel_id
        result['DeliveryChannelName'] = self.delivery_channel_name
        result['DeliveryChannelType'] = self.delivery_channel_type
        result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        result['DeliveryChannelCondition'] = self.delivery_channel_condition
        result['Description'] = self.description
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.delivery_channel_id = map.get('DeliveryChannelId')
        self.delivery_channel_name = map.get('DeliveryChannelName')
        self.delivery_channel_type = map.get('DeliveryChannelType')
        self.delivery_channel_target_arn = map.get('DeliveryChannelTargetArn')
        self.delivery_channel_assume_role_arn = map.get('DeliveryChannelAssumeRoleArn')
        self.delivery_channel_condition = map.get('DeliveryChannelCondition')
        self.description = map.get('Description')
        self.status = map.get('Status')
        return self


class PutConfigurationRecorderRequest(TeaModel):
    def __init__(self, resource_types=None):
        self.resource_types = resource_types  # type: str

    def validate(self):
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = {}
        result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        self.resource_types = map.get('ResourceTypes')
        return self


class PutConfigurationRecorderResponse(TeaModel):
    def __init__(self, request_id=None, configuration_recorder=None):
        self.request_id = request_id    # type: str
        self.configuration_recorder = configuration_recorder  # type: PutConfigurationRecorderResponseConfigurationRecorder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.configuration_recorder, 'configuration_recorder')
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()
        else:
            result['ConfigurationRecorder'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ConfigurationRecorder') is not None:
            temp_model = PutConfigurationRecorderResponseConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(map['ConfigurationRecorder'])
        else:
            self.configuration_recorder = None
        return self


class PutConfigurationRecorderResponseConfigurationRecorder(TeaModel):
    def __init__(self, account_id=None, configuration_recorder_status=None, organization_master_id=None,
                 organization_enable_status=None, resource_types=None):
        self.account_id = account_id    # type: int
        self.configuration_recorder_status = configuration_recorder_status  # type: str
        self.organization_master_id = organization_master_id  # type: int
        self.organization_enable_status = organization_enable_status  # type: str
        self.resource_types = resource_types  # type: List[str]

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.configuration_recorder_status, 'configuration_recorder_status')
        self.validate_required(self.organization_master_id, 'organization_master_id')
        self.validate_required(self.organization_enable_status, 'organization_enable_status')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['ConfigurationRecorderStatus'] = self.configuration_recorder_status
        result['OrganizationMasterId'] = self.organization_master_id
        result['OrganizationEnableStatus'] = self.organization_enable_status
        result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.configuration_recorder_status = map.get('ConfigurationRecorderStatus')
        self.organization_master_id = map.get('OrganizationMasterId')
        self.organization_enable_status = map.get('OrganizationEnableStatus')
        self.resource_types = map.get('ResourceTypes')
        return self


class GetDiscoveredResourceSummaryRequest(TeaModel):
    def __init__(self, multi_account=None, member_id=None):
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class GetDiscoveredResourceSummaryResponse(TeaModel):
    def __init__(self, request_id=None, discovered_resource_summary=None):
        self.request_id = request_id    # type: str
        self.discovered_resource_summary = discovered_resource_summary  # type: GetDiscoveredResourceSummaryResponseDiscoveredResourceSummary

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.discovered_resource_summary, 'discovered_resource_summary')
        if self.discovered_resource_summary:
            self.discovered_resource_summary.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.discovered_resource_summary is not None:
            result['DiscoveredResourceSummary'] = self.discovered_resource_summary.to_map()
        else:
            result['DiscoveredResourceSummary'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DiscoveredResourceSummary') is not None:
            temp_model = GetDiscoveredResourceSummaryResponseDiscoveredResourceSummary()
            self.discovered_resource_summary = temp_model.from_map(map['DiscoveredResourceSummary'])
        else:
            self.discovered_resource_summary = None
        return self


class GetDiscoveredResourceSummaryResponseDiscoveredResourceSummary(TeaModel):
    def __init__(self, resource_count=None, resource_type_count=None, region_count=None):
        self.resource_count = resource_count  # type: int
        self.resource_type_count = resource_type_count  # type: int
        self.region_count = region_count  # type: int

    def validate(self):
        self.validate_required(self.resource_count, 'resource_count')
        self.validate_required(self.resource_type_count, 'resource_type_count')
        self.validate_required(self.region_count, 'region_count')

    def to_map(self):
        result = {}
        result['ResourceCount'] = self.resource_count
        result['ResourceTypeCount'] = self.resource_type_count
        result['RegionCount'] = self.region_count
        return result

    def from_map(self, map={}):
        self.resource_count = map.get('ResourceCount')
        self.resource_type_count = map.get('ResourceTypeCount')
        self.region_count = map.get('RegionCount')
        return self


class ActiveConfigRulesRequest(TeaModel):
    def __init__(self, config_rule_ids=None):
        self.config_rule_ids = config_rule_ids  # type: str

    def validate(self):
        self.validate_required(self.config_rule_ids, 'config_rule_ids')

    def to_map(self):
        result = {}
        result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, map={}):
        self.config_rule_ids = map.get('ConfigRuleIds')
        return self


class ActiveConfigRulesResponse(TeaModel):
    def __init__(self, request_id=None, operate_rule_result=None):
        self.request_id = request_id    # type: str
        self.operate_rule_result = operate_rule_result  # type: ActiveConfigRulesResponseOperateRuleResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operate_rule_result, 'operate_rule_result')
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        else:
            result['OperateRuleResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('OperateRuleResult') is not None:
            temp_model = ActiveConfigRulesResponseOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(map['OperateRuleResult'])
        else:
            self.operate_rule_result = None
        return self


class ActiveConfigRulesResponseOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(self, config_rule_id=None, error_code=None, success=None):
        self.config_rule_id = config_rule_id  # type: str
        self.error_code = error_code    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        return self


class ActiveConfigRulesResponseOperateRuleResult(TeaModel):
    def __init__(self, operate_rule_item_list=None):
        self.operate_rule_item_list = operate_rule_item_list  # type: List[ActiveConfigRulesResponseOperateRuleResultOperateRuleItemList]

    def validate(self):
        self.validate_required(self.operate_rule_item_list, 'operate_rule_item_list')
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        else:
            result['OperateRuleItemList'] = None
        return result

    def from_map(self, map={}):
        self.operate_rule_item_list = []
        if map.get('OperateRuleItemList') is not None:
            for k in map.get('OperateRuleItemList'):
                temp_model = ActiveConfigRulesResponseOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        else:
            self.operate_rule_item_list = None
        return self


class StopConfigRulesRequest(TeaModel):
    def __init__(self, config_rule_ids=None):
        self.config_rule_ids = config_rule_ids  # type: str

    def validate(self):
        self.validate_required(self.config_rule_ids, 'config_rule_ids')

    def to_map(self):
        result = {}
        result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, map={}):
        self.config_rule_ids = map.get('ConfigRuleIds')
        return self


class StopConfigRulesResponse(TeaModel):
    def __init__(self, request_id=None, operate_rule_result=None):
        self.request_id = request_id    # type: str
        self.operate_rule_result = operate_rule_result  # type: StopConfigRulesResponseOperateRuleResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operate_rule_result, 'operate_rule_result')
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        else:
            result['OperateRuleResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('OperateRuleResult') is not None:
            temp_model = StopConfigRulesResponseOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(map['OperateRuleResult'])
        else:
            self.operate_rule_result = None
        return self


class StopConfigRulesResponseOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(self, config_rule_id=None, error_code=None, success=None):
        self.config_rule_id = config_rule_id  # type: str
        self.error_code = error_code    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        return self


class StopConfigRulesResponseOperateRuleResult(TeaModel):
    def __init__(self, operate_rule_item_list=None):
        self.operate_rule_item_list = operate_rule_item_list  # type: List[StopConfigRulesResponseOperateRuleResultOperateRuleItemList]

    def validate(self):
        self.validate_required(self.operate_rule_item_list, 'operate_rule_item_list')
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        else:
            result['OperateRuleItemList'] = None
        return result

    def from_map(self, map={}):
        self.operate_rule_item_list = []
        if map.get('OperateRuleItemList') is not None:
            for k in map.get('OperateRuleItemList'):
                temp_model = StopConfigRulesResponseOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        else:
            self.operate_rule_item_list = None
        return self


class DescribeComplianceSummaryRequest(TeaModel):
    def __init__(self, multi_account=None, member_id=None):
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class DescribeComplianceSummaryResponse(TeaModel):
    def __init__(self, request_id=None, compliance_summary=None):
        self.request_id = request_id    # type: str
        self.compliance_summary = compliance_summary  # type: DescribeComplianceSummaryResponseComplianceSummary

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.compliance_summary, 'compliance_summary')
        if self.compliance_summary:
            self.compliance_summary.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.compliance_summary is not None:
            result['ComplianceSummary'] = self.compliance_summary.to_map()
        else:
            result['ComplianceSummary'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ComplianceSummary') is not None:
            temp_model = DescribeComplianceSummaryResponseComplianceSummary()
            self.compliance_summary = temp_model.from_map(map['ComplianceSummary'])
        else:
            self.compliance_summary = None
        return self


class DescribeComplianceSummaryResponseComplianceSummaryComplianceSummaryByConfigRule(TeaModel):
    def __init__(self, compliance_summary_timestamp=None, compliant_count=None, non_compliant_count=None,
                 total_count=None):
        self.compliance_summary_timestamp = compliance_summary_timestamp  # type: int
        self.compliant_count = compliant_count  # type: int
        self.non_compliant_count = non_compliant_count  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        self.validate_required(self.compliance_summary_timestamp, 'compliance_summary_timestamp')
        self.validate_required(self.compliant_count, 'compliant_count')
        self.validate_required(self.non_compliant_count, 'non_compliant_count')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = {}
        result['ComplianceSummaryTimestamp'] = self.compliance_summary_timestamp
        result['CompliantCount'] = self.compliant_count
        result['NonCompliantCount'] = self.non_compliant_count
        result['TotalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.compliance_summary_timestamp = map.get('ComplianceSummaryTimestamp')
        self.compliant_count = map.get('CompliantCount')
        self.non_compliant_count = map.get('NonCompliantCount')
        self.total_count = map.get('TotalCount')
        return self


class DescribeComplianceSummaryResponseComplianceSummaryComplianceSummaryByResource(TeaModel):
    def __init__(self, compliance_summary_timestamp=None, compliant_count=None, non_compliant_count=None,
                 total_count=None):
        self.compliance_summary_timestamp = compliance_summary_timestamp  # type: int
        self.compliant_count = compliant_count  # type: int
        self.non_compliant_count = non_compliant_count  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        self.validate_required(self.compliance_summary_timestamp, 'compliance_summary_timestamp')
        self.validate_required(self.compliant_count, 'compliant_count')
        self.validate_required(self.non_compliant_count, 'non_compliant_count')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = {}
        result['ComplianceSummaryTimestamp'] = self.compliance_summary_timestamp
        result['CompliantCount'] = self.compliant_count
        result['NonCompliantCount'] = self.non_compliant_count
        result['TotalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.compliance_summary_timestamp = map.get('ComplianceSummaryTimestamp')
        self.compliant_count = map.get('CompliantCount')
        self.non_compliant_count = map.get('NonCompliantCount')
        self.total_count = map.get('TotalCount')
        return self


class DescribeComplianceSummaryResponseComplianceSummary(TeaModel):
    def __init__(self, compliance_summary_by_config_rule=None, compliance_summary_by_resource=None):
        self.compliance_summary_by_config_rule = compliance_summary_by_config_rule  # type: DescribeComplianceSummaryResponseComplianceSummaryComplianceSummaryByConfigRule
        self.compliance_summary_by_resource = compliance_summary_by_resource  # type: DescribeComplianceSummaryResponseComplianceSummaryComplianceSummaryByResource

    def validate(self):
        self.validate_required(self.compliance_summary_by_config_rule, 'compliance_summary_by_config_rule')
        if self.compliance_summary_by_config_rule:
            self.compliance_summary_by_config_rule.validate()
        self.validate_required(self.compliance_summary_by_resource, 'compliance_summary_by_resource')
        if self.compliance_summary_by_resource:
            self.compliance_summary_by_resource.validate()

    def to_map(self):
        result = {}
        if self.compliance_summary_by_config_rule is not None:
            result['ComplianceSummaryByConfigRule'] = self.compliance_summary_by_config_rule.to_map()
        else:
            result['ComplianceSummaryByConfigRule'] = None
        if self.compliance_summary_by_resource is not None:
            result['ComplianceSummaryByResource'] = self.compliance_summary_by_resource.to_map()
        else:
            result['ComplianceSummaryByResource'] = None
        return result

    def from_map(self, map={}):
        if map.get('ComplianceSummaryByConfigRule') is not None:
            temp_model = DescribeComplianceSummaryResponseComplianceSummaryComplianceSummaryByConfigRule()
            self.compliance_summary_by_config_rule = temp_model.from_map(map['ComplianceSummaryByConfigRule'])
        else:
            self.compliance_summary_by_config_rule = None
        if map.get('ComplianceSummaryByResource') is not None:
            temp_model = DescribeComplianceSummaryResponseComplianceSummaryComplianceSummaryByResource()
            self.compliance_summary_by_resource = temp_model.from_map(map['ComplianceSummaryByResource'])
        else:
            self.compliance_summary_by_resource = None
        return self


class ListConfigRulesRequest(TeaModel):
    def __init__(self, config_rule_state=None, compliance_type=None, risk_level=None, message_type=None,
                 page_number=None, page_size=None, multi_account=None, member_id=None):
        self.config_rule_state = config_rule_state  # type: str
        self.compliance_type = compliance_type  # type: str
        self.risk_level = risk_level    # type: int
        self.message_type = message_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ConfigRuleState'] = self.config_rule_state
        result['ComplianceType'] = self.compliance_type
        result['RiskLevel'] = self.risk_level
        result['MessageType'] = self.message_type
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.config_rule_state = map.get('ConfigRuleState')
        self.compliance_type = map.get('ComplianceType')
        self.risk_level = map.get('RiskLevel')
        self.message_type = map.get('MessageType')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class ListConfigRulesResponse(TeaModel):
    def __init__(self, request_id=None, config_rules=None):
        self.request_id = request_id    # type: str
        self.config_rules = config_rules  # type: ListConfigRulesResponseConfigRules

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.config_rules, 'config_rules')
        if self.config_rules:
            self.config_rules.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.config_rules is not None:
            result['ConfigRules'] = self.config_rules.to_map()
        else:
            result['ConfigRules'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ConfigRules') is not None:
            temp_model = ListConfigRulesResponseConfigRules()
            self.config_rules = temp_model.from_map(map['ConfigRules'])
        else:
            self.config_rules = None
        return self


class ListConfigRulesResponseConfigRulesConfigRuleListCompliance(TeaModel):
    def __init__(self, compliance_type=None, count=None):
        self.compliance_type = compliance_type  # type: str
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.compliance_type, 'compliance_type')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['ComplianceType'] = self.compliance_type
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.compliance_type = map.get('ComplianceType')
        self.count = map.get('Count')
        return self


class ListConfigRulesResponseConfigRulesConfigRuleListCreateBy(TeaModel):
    def __init__(self, creator_id=None, creator_name=None, creator_type=None, config_rule_scene_id=None,
                 config_rule_scene_name=None):
        self.creator_id = creator_id    # type: str
        self.creator_name = creator_name  # type: str
        self.creator_type = creator_type  # type: str
        self.config_rule_scene_id = config_rule_scene_id  # type: str
        self.config_rule_scene_name = config_rule_scene_name  # type: str

    def validate(self):
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.creator_name, 'creator_name')
        self.validate_required(self.creator_type, 'creator_type')
        self.validate_required(self.config_rule_scene_id, 'config_rule_scene_id')
        self.validate_required(self.config_rule_scene_name, 'config_rule_scene_name')

    def to_map(self):
        result = {}
        result['CreatorId'] = self.creator_id
        result['CreatorName'] = self.creator_name
        result['CreatorType'] = self.creator_type
        result['ConfigRuleSceneId'] = self.config_rule_scene_id
        result['ConfigRuleSceneName'] = self.config_rule_scene_name
        return result

    def from_map(self, map={}):
        self.creator_id = map.get('CreatorId')
        self.creator_name = map.get('CreatorName')
        self.creator_type = map.get('CreatorType')
        self.config_rule_scene_id = map.get('ConfigRuleSceneId')
        self.config_rule_scene_name = map.get('ConfigRuleSceneName')
        return self


class ListConfigRulesResponseConfigRulesConfigRuleList(TeaModel):
    def __init__(self, account_id=None, config_rule_arn=None, config_rule_id=None, config_rule_name=None,
                 config_rule_state=None, description=None, risk_level=None, source_identifier=None, source_owner=None,
                 automation_type=None, compliance=None, create_by=None):
        self.account_id = account_id    # type: int
        self.config_rule_arn = config_rule_arn  # type: str
        self.config_rule_id = config_rule_id  # type: str
        self.config_rule_name = config_rule_name  # type: str
        self.config_rule_state = config_rule_state  # type: str
        self.description = description  # type: str
        self.risk_level = risk_level    # type: int
        self.source_identifier = source_identifier  # type: str
        self.source_owner = source_owner  # type: str
        self.automation_type = automation_type  # type: str
        self.compliance = compliance    # type: ListConfigRulesResponseConfigRulesConfigRuleListCompliance
        self.create_by = create_by      # type: ListConfigRulesResponseConfigRulesConfigRuleListCreateBy

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.config_rule_arn, 'config_rule_arn')
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.config_rule_name, 'config_rule_name')
        self.validate_required(self.config_rule_state, 'config_rule_state')
        self.validate_required(self.description, 'description')
        self.validate_required(self.risk_level, 'risk_level')
        self.validate_required(self.source_identifier, 'source_identifier')
        self.validate_required(self.source_owner, 'source_owner')
        self.validate_required(self.automation_type, 'automation_type')
        self.validate_required(self.compliance, 'compliance')
        if self.compliance:
            self.compliance.validate()
        self.validate_required(self.create_by, 'create_by')
        if self.create_by:
            self.create_by.validate()

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['ConfigRuleArn'] = self.config_rule_arn
        result['ConfigRuleId'] = self.config_rule_id
        result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleState'] = self.config_rule_state
        result['Description'] = self.description
        result['RiskLevel'] = self.risk_level
        result['SourceIdentifier'] = self.source_identifier
        result['SourceOwner'] = self.source_owner
        result['AutomationType'] = self.automation_type
        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()
        else:
            result['Compliance'] = None
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        else:
            result['CreateBy'] = None
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.config_rule_arn = map.get('ConfigRuleArn')
        self.config_rule_id = map.get('ConfigRuleId')
        self.config_rule_name = map.get('ConfigRuleName')
        self.config_rule_state = map.get('ConfigRuleState')
        self.description = map.get('Description')
        self.risk_level = map.get('RiskLevel')
        self.source_identifier = map.get('SourceIdentifier')
        self.source_owner = map.get('SourceOwner')
        self.automation_type = map.get('AutomationType')
        if map.get('Compliance') is not None:
            temp_model = ListConfigRulesResponseConfigRulesConfigRuleListCompliance()
            self.compliance = temp_model.from_map(map['Compliance'])
        else:
            self.compliance = None
        if map.get('CreateBy') is not None:
            temp_model = ListConfigRulesResponseConfigRulesConfigRuleListCreateBy()
            self.create_by = temp_model.from_map(map['CreateBy'])
        else:
            self.create_by = None
        return self


class ListConfigRulesResponseConfigRules(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, config_rule_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.config_rule_list = config_rule_list  # type: List[ListConfigRulesResponseConfigRulesConfigRuleList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.config_rule_list, 'config_rule_list')
        if self.config_rule_list:
            for k in self.config_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['ConfigRuleList'] = []
        if self.config_rule_list is not None:
            for k in self.config_rule_list:
                result['ConfigRuleList'].append(k.to_map() if k else None)
        else:
            result['ConfigRuleList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.config_rule_list = []
        if map.get('ConfigRuleList') is not None:
            for k in map.get('ConfigRuleList'):
                temp_model = ListConfigRulesResponseConfigRulesConfigRuleList()
                self.config_rule_list.append(temp_model.from_map(k))
        else:
            self.config_rule_list = None
        return self


class PutConfigRuleRequest(TeaModel):
    def __init__(self, config_rule_id=None, config_rule_name=None, description=None, input_parameters=None,
                 source_owner=None, source_identifier=None, source_detail_message_type=None,
                 source_maximum_execution_frequency=None, scope_compliance_resource_id=None, scope_compliance_resource_types=None, risk_level=None,
                 client_token=None, multi_account=None, member_id=None):
        self.config_rule_id = config_rule_id  # type: str
        self.config_rule_name = config_rule_name  # type: str
        self.description = description  # type: str
        self.input_parameters = input_parameters  # type: str
        self.source_owner = source_owner  # type: str
        self.source_identifier = source_identifier  # type: str
        self.source_detail_message_type = source_detail_message_type  # type: str
        self.source_maximum_execution_frequency = source_maximum_execution_frequency  # type: str
        self.scope_compliance_resource_id = scope_compliance_resource_id  # type: str
        self.scope_compliance_resource_types = scope_compliance_resource_types  # type: str
        self.risk_level = risk_level    # type: int
        self.client_token = client_token  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        self.validate_required(self.config_rule_name, 'config_rule_name')
        self.validate_required(self.source_owner, 'source_owner')
        self.validate_required(self.source_identifier, 'source_identifier')
        self.validate_required(self.source_detail_message_type, 'source_detail_message_type')
        self.validate_required(self.scope_compliance_resource_types, 'scope_compliance_resource_types')
        self.validate_required(self.risk_level, 'risk_level')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['ConfigRuleName'] = self.config_rule_name
        result['Description'] = self.description
        result['InputParameters'] = self.input_parameters
        result['SourceOwner'] = self.source_owner
        result['SourceIdentifier'] = self.source_identifier
        result['SourceDetailMessageType'] = self.source_detail_message_type
        result['SourceMaximumExecutionFrequency'] = self.source_maximum_execution_frequency
        result['ScopeComplianceResourceId'] = self.scope_compliance_resource_id
        result['ScopeComplianceResourceTypes'] = self.scope_compliance_resource_types
        result['RiskLevel'] = self.risk_level
        result['ClientToken'] = self.client_token
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.config_rule_name = map.get('ConfigRuleName')
        self.description = map.get('Description')
        self.input_parameters = map.get('InputParameters')
        self.source_owner = map.get('SourceOwner')
        self.source_identifier = map.get('SourceIdentifier')
        self.source_detail_message_type = map.get('SourceDetailMessageType')
        self.source_maximum_execution_frequency = map.get('SourceMaximumExecutionFrequency')
        self.scope_compliance_resource_id = map.get('ScopeComplianceResourceId')
        self.scope_compliance_resource_types = map.get('ScopeComplianceResourceTypes')
        self.risk_level = map.get('RiskLevel')
        self.client_token = map.get('ClientToken')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class PutConfigRuleResponse(TeaModel):
    def __init__(self, config_rule_id=None, request_id=None):
        self.config_rule_id = config_rule_id  # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.request_id = map.get('RequestId')
        return self


class DescribeEvaluationResultsRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, compliance_type=None, page_number=None, page_size=None,
                 config_rule_id=None, multi_account=None, member_id=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.compliance_type = compliance_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.config_rule_id = config_rule_id  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['ComplianceType'] = self.compliance_type
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ConfigRuleId'] = self.config_rule_id
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.compliance_type = map.get('ComplianceType')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.config_rule_id = map.get('ConfigRuleId')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class DescribeEvaluationResultsResponse(TeaModel):
    def __init__(self, request_id=None, evaluation_results=None):
        self.request_id = request_id    # type: str
        self.evaluation_results = evaluation_results  # type: DescribeEvaluationResultsResponseEvaluationResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.evaluation_results, 'evaluation_results')
        if self.evaluation_results:
            self.evaluation_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results.to_map()
        else:
            result['EvaluationResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('EvaluationResults') is not None:
            temp_model = DescribeEvaluationResultsResponseEvaluationResults()
            self.evaluation_results = temp_model.from_map(map['EvaluationResults'])
        else:
            self.evaluation_results = None
        return self


class DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier(TeaModel):
    def __init__(self, config_rule_arn=None, config_rule_id=None, config_rule_name=None, resource_id=None,
                 resource_type=None, region_id=None):
        self.config_rule_arn = config_rule_arn  # type: str
        self.config_rule_id = config_rule_id  # type: str
        self.config_rule_name = config_rule_name  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.config_rule_arn, 'config_rule_arn')
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.config_rule_name, 'config_rule_name')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ConfigRuleArn'] = self.config_rule_arn
        result['ConfigRuleId'] = self.config_rule_id
        result['ConfigRuleName'] = self.config_rule_name
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.config_rule_arn = map.get('ConfigRuleArn')
        self.config_rule_id = map.get('ConfigRuleId')
        self.config_rule_name = map.get('ConfigRuleName')
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.region_id = map.get('RegionId')
        return self


class DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultListEvaluationResultIdentifier(TeaModel):
    def __init__(self, ordering_timestamp=None, evaluation_result_qualifier=None):
        self.ordering_timestamp = ordering_timestamp  # type: int
        self.evaluation_result_qualifier = evaluation_result_qualifier  # type: DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier

    def validate(self):
        self.validate_required(self.ordering_timestamp, 'ordering_timestamp')
        self.validate_required(self.evaluation_result_qualifier, 'evaluation_result_qualifier')
        if self.evaluation_result_qualifier:
            self.evaluation_result_qualifier.validate()

    def to_map(self):
        result = {}
        result['OrderingTimestamp'] = self.ordering_timestamp
        if self.evaluation_result_qualifier is not None:
            result['EvaluationResultQualifier'] = self.evaluation_result_qualifier.to_map()
        else:
            result['EvaluationResultQualifier'] = None
        return result

    def from_map(self, map={}):
        self.ordering_timestamp = map.get('OrderingTimestamp')
        if map.get('EvaluationResultQualifier') is not None:
            temp_model = DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultListEvaluationResultIdentifierEvaluationResultQualifier()
            self.evaluation_result_qualifier = temp_model.from_map(map['EvaluationResultQualifier'])
        else:
            self.evaluation_result_qualifier = None
        return self


class DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultList(TeaModel):
    def __init__(self, annotation=None, compliance_type=None, config_rule_invoked_timestamp=None,
                 invoking_event_message_type=None, result_recorded_timestamp=None, risk_level=None, evaluation_result_identifier=None):
        self.annotation = annotation    # type: str
        self.compliance_type = compliance_type  # type: str
        self.config_rule_invoked_timestamp = config_rule_invoked_timestamp  # type: int
        self.invoking_event_message_type = invoking_event_message_type  # type: str
        self.result_recorded_timestamp = result_recorded_timestamp  # type: int
        self.risk_level = risk_level    # type: int
        self.evaluation_result_identifier = evaluation_result_identifier  # type: DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultListEvaluationResultIdentifier

    def validate(self):
        self.validate_required(self.annotation, 'annotation')
        self.validate_required(self.compliance_type, 'compliance_type')
        self.validate_required(self.config_rule_invoked_timestamp, 'config_rule_invoked_timestamp')
        self.validate_required(self.invoking_event_message_type, 'invoking_event_message_type')
        self.validate_required(self.result_recorded_timestamp, 'result_recorded_timestamp')
        self.validate_required(self.risk_level, 'risk_level')
        self.validate_required(self.evaluation_result_identifier, 'evaluation_result_identifier')
        if self.evaluation_result_identifier:
            self.evaluation_result_identifier.validate()

    def to_map(self):
        result = {}
        result['Annotation'] = self.annotation
        result['ComplianceType'] = self.compliance_type
        result['ConfigRuleInvokedTimestamp'] = self.config_rule_invoked_timestamp
        result['InvokingEventMessageType'] = self.invoking_event_message_type
        result['ResultRecordedTimestamp'] = self.result_recorded_timestamp
        result['RiskLevel'] = self.risk_level
        if self.evaluation_result_identifier is not None:
            result['EvaluationResultIdentifier'] = self.evaluation_result_identifier.to_map()
        else:
            result['EvaluationResultIdentifier'] = None
        return result

    def from_map(self, map={}):
        self.annotation = map.get('Annotation')
        self.compliance_type = map.get('ComplianceType')
        self.config_rule_invoked_timestamp = map.get('ConfigRuleInvokedTimestamp')
        self.invoking_event_message_type = map.get('InvokingEventMessageType')
        self.result_recorded_timestamp = map.get('ResultRecordedTimestamp')
        self.risk_level = map.get('RiskLevel')
        if map.get('EvaluationResultIdentifier') is not None:
            temp_model = DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultListEvaluationResultIdentifier()
            self.evaluation_result_identifier = temp_model.from_map(map['EvaluationResultIdentifier'])
        else:
            self.evaluation_result_identifier = None
        return self


class DescribeEvaluationResultsResponseEvaluationResults(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, evaluation_result_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.evaluation_result_list = evaluation_result_list  # type: List[DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.evaluation_result_list, 'evaluation_result_list')
        if self.evaluation_result_list:
            for k in self.evaluation_result_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['EvaluationResultList'] = []
        if self.evaluation_result_list is not None:
            for k in self.evaluation_result_list:
                result['EvaluationResultList'].append(k.to_map() if k else None)
        else:
            result['EvaluationResultList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.evaluation_result_list = []
        if map.get('EvaluationResultList') is not None:
            for k in map.get('EvaluationResultList'):
                temp_model = DescribeEvaluationResultsResponseEvaluationResultsEvaluationResultList()
                self.evaluation_result_list.append(temp_model.from_map(k))
        else:
            self.evaluation_result_list = None
        return self


class DeleteConfigRulesRequest(TeaModel):
    def __init__(self, config_rule_ids=None):
        self.config_rule_ids = config_rule_ids  # type: str

    def validate(self):
        self.validate_required(self.config_rule_ids, 'config_rule_ids')

    def to_map(self):
        result = {}
        result['ConfigRuleIds'] = self.config_rule_ids
        return result

    def from_map(self, map={}):
        self.config_rule_ids = map.get('ConfigRuleIds')
        return self


class DeleteConfigRulesResponse(TeaModel):
    def __init__(self, request_id=None, operate_rule_result=None):
        self.request_id = request_id    # type: str
        self.operate_rule_result = operate_rule_result  # type: DeleteConfigRulesResponseOperateRuleResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operate_rule_result, 'operate_rule_result')
        if self.operate_rule_result:
            self.operate_rule_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.operate_rule_result is not None:
            result['OperateRuleResult'] = self.operate_rule_result.to_map()
        else:
            result['OperateRuleResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('OperateRuleResult') is not None:
            temp_model = DeleteConfigRulesResponseOperateRuleResult()
            self.operate_rule_result = temp_model.from_map(map['OperateRuleResult'])
        else:
            self.operate_rule_result = None
        return self


class DeleteConfigRulesResponseOperateRuleResultOperateRuleItemList(TeaModel):
    def __init__(self, config_rule_id=None, error_code=None, success=None):
        self.config_rule_id = config_rule_id  # type: str
        self.error_code = error_code    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        return self


class DeleteConfigRulesResponseOperateRuleResult(TeaModel):
    def __init__(self, operate_rule_item_list=None):
        self.operate_rule_item_list = operate_rule_item_list  # type: List[DeleteConfigRulesResponseOperateRuleResultOperateRuleItemList]

    def validate(self):
        self.validate_required(self.operate_rule_item_list, 'operate_rule_item_list')
        if self.operate_rule_item_list:
            for k in self.operate_rule_item_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['OperateRuleItemList'] = []
        if self.operate_rule_item_list is not None:
            for k in self.operate_rule_item_list:
                result['OperateRuleItemList'].append(k.to_map() if k else None)
        else:
            result['OperateRuleItemList'] = None
        return result

    def from_map(self, map={}):
        self.operate_rule_item_list = []
        if map.get('OperateRuleItemList') is not None:
            for k in map.get('OperateRuleItemList'):
                temp_model = DeleteConfigRulesResponseOperateRuleResultOperateRuleItemList()
                self.operate_rule_item_list.append(temp_model.from_map(k))
        else:
            self.operate_rule_item_list = None
        return self


class DescribeComplianceRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, compliance_type=None, config_rule_id=None,
                 multi_account=None, member_id=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.compliance_type = compliance_type  # type: str
        self.config_rule_id = config_rule_id  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['ComplianceType'] = self.compliance_type
        result['ConfigRuleId'] = self.config_rule_id
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.compliance_type = map.get('ComplianceType')
        self.config_rule_id = map.get('ConfigRuleId')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class DescribeComplianceResponse(TeaModel):
    def __init__(self, request_id=None, compliance_result=None):
        self.request_id = request_id    # type: str
        self.compliance_result = compliance_result  # type: DescribeComplianceResponseComplianceResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.compliance_result, 'compliance_result')
        if self.compliance_result:
            self.compliance_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.compliance_result is not None:
            result['ComplianceResult'] = self.compliance_result.to_map()
        else:
            result['ComplianceResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ComplianceResult') is not None:
            temp_model = DescribeComplianceResponseComplianceResult()
            self.compliance_result = temp_model.from_map(map['ComplianceResult'])
        else:
            self.compliance_result = None
        return self


class DescribeComplianceResponseComplianceResultCompliances(TeaModel):
    def __init__(self, compliance_type=None, count=None):
        self.compliance_type = compliance_type  # type: str
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.compliance_type, 'compliance_type')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['ComplianceType'] = self.compliance_type
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.compliance_type = map.get('ComplianceType')
        self.count = map.get('Count')
        return self


class DescribeComplianceResponseComplianceResult(TeaModel):
    def __init__(self, total_count=None, compliances=None):
        self.total_count = total_count  # type: int
        self.compliances = compliances  # type: List[DescribeComplianceResponseComplianceResultCompliances]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.compliances, 'compliances')
        if self.compliances:
            for k in self.compliances:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['Compliances'] = []
        if self.compliances is not None:
            for k in self.compliances:
                result['Compliances'].append(k.to_map() if k else None)
        else:
            result['Compliances'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.compliances = []
        if map.get('Compliances') is not None:
            for k in map.get('Compliances'):
                temp_model = DescribeComplianceResponseComplianceResultCompliances()
                self.compliances.append(temp_model.from_map(k))
        else:
            self.compliances = None
        return self


class GetDiscoveredResourceCountsRequest(TeaModel):
    def __init__(self, group_by_key=None, multi_account=None, member_id=None):
        self.group_by_key = group_by_key  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['GroupByKey'] = self.group_by_key
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.group_by_key = map.get('GroupByKey')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class GetDiscoveredResourceCountsResponse(TeaModel):
    def __init__(self, request_id=None, grouped_resource_counts=None):
        self.request_id = request_id    # type: str
        self.grouped_resource_counts = grouped_resource_counts  # type: GetDiscoveredResourceCountsResponseGroupedResourceCounts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.grouped_resource_counts, 'grouped_resource_counts')
        if self.grouped_resource_counts:
            self.grouped_resource_counts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.grouped_resource_counts is not None:
            result['GroupedResourceCounts'] = self.grouped_resource_counts.to_map()
        else:
            result['GroupedResourceCounts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('GroupedResourceCounts') is not None:
            temp_model = GetDiscoveredResourceCountsResponseGroupedResourceCounts()
            self.grouped_resource_counts = temp_model.from_map(map['GroupedResourceCounts'])
        else:
            self.grouped_resource_counts = None
        return self


class GetDiscoveredResourceCountsResponseGroupedResourceCountsGroupedResourceCountList(TeaModel):
    def __init__(self, group_name=None, resource_count=None):
        self.group_name = group_name    # type: str
        self.resource_count = resource_count  # type: int

    def validate(self):
        self.validate_required(self.group_name, 'group_name')
        self.validate_required(self.resource_count, 'resource_count')

    def to_map(self):
        result = {}
        result['GroupName'] = self.group_name
        result['ResourceCount'] = self.resource_count
        return result

    def from_map(self, map={}):
        self.group_name = map.get('GroupName')
        self.resource_count = map.get('ResourceCount')
        return self


class GetDiscoveredResourceCountsResponseGroupedResourceCounts(TeaModel):
    def __init__(self, group_by_key=None, grouped_resource_count_list=None):
        self.group_by_key = group_by_key  # type: str
        self.grouped_resource_count_list = grouped_resource_count_list  # type: List[GetDiscoveredResourceCountsResponseGroupedResourceCountsGroupedResourceCountList]

    def validate(self):
        self.validate_required(self.group_by_key, 'group_by_key')
        self.validate_required(self.grouped_resource_count_list, 'grouped_resource_count_list')
        if self.grouped_resource_count_list:
            for k in self.grouped_resource_count_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['GroupByKey'] = self.group_by_key
        result['GroupedResourceCountList'] = []
        if self.grouped_resource_count_list is not None:
            for k in self.grouped_resource_count_list:
                result['GroupedResourceCountList'].append(k.to_map() if k else None)
        else:
            result['GroupedResourceCountList'] = None
        return result

    def from_map(self, map={}):
        self.group_by_key = map.get('GroupByKey')
        self.grouped_resource_count_list = []
        if map.get('GroupedResourceCountList') is not None:
            for k in map.get('GroupedResourceCountList'):
                temp_model = GetDiscoveredResourceCountsResponseGroupedResourceCountsGroupedResourceCountList()
                self.grouped_resource_count_list.append(temp_model.from_map(k))
        else:
            self.grouped_resource_count_list = None
        return self


class ListDiscoveredResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_deleted=None, page_size=None, page_number=None,
                 resource_types=None, regions=None, compliance_type=None, multi_account=None, member_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_deleted = resource_deleted  # type: int
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.resource_types = resource_types  # type: str
        self.regions = regions          # type: str
        self.compliance_type = compliance_type  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceDeleted'] = self.resource_deleted
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['ResourceTypes'] = self.resource_types
        result['Regions'] = self.regions
        result['ComplianceType'] = self.compliance_type
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_deleted = map.get('ResourceDeleted')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.resource_types = map.get('ResourceTypes')
        self.regions = map.get('Regions')
        self.compliance_type = map.get('ComplianceType')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class ListDiscoveredResourcesResponse(TeaModel):
    def __init__(self, request_id=None, discovered_resource_profiles=None):
        self.request_id = request_id    # type: str
        self.discovered_resource_profiles = discovered_resource_profiles  # type: ListDiscoveredResourcesResponseDiscoveredResourceProfiles

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.discovered_resource_profiles, 'discovered_resource_profiles')
        if self.discovered_resource_profiles:
            self.discovered_resource_profiles.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.discovered_resource_profiles is not None:
            result['DiscoveredResourceProfiles'] = self.discovered_resource_profiles.to_map()
        else:
            result['DiscoveredResourceProfiles'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DiscoveredResourceProfiles') is not None:
            temp_model = ListDiscoveredResourcesResponseDiscoveredResourceProfiles()
            self.discovered_resource_profiles = temp_model.from_map(map['DiscoveredResourceProfiles'])
        else:
            self.discovered_resource_profiles = None
        return self


class ListDiscoveredResourcesResponseDiscoveredResourceProfilesDiscoveredResourceProfileList(TeaModel):
    def __init__(self, account_id=None, region=None, resource_creation_time=None, resource_deleted=None,
                 resource_id=None, resource_name=None, resource_status=None, resource_type=None, tags=None):
        self.account_id = account_id    # type: int
        self.region = region            # type: str
        self.resource_creation_time = resource_creation_time  # type: int
        self.resource_deleted = resource_deleted  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_status = resource_status  # type: str
        self.resource_type = resource_type  # type: str
        self.tags = tags                # type: str

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.resource_creation_time, 'resource_creation_time')
        self.validate_required(self.resource_deleted, 'resource_deleted')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.resource_status, 'resource_status')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tags, 'tags')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['Region'] = self.region
        result['ResourceCreationTime'] = self.resource_creation_time
        result['ResourceDeleted'] = self.resource_deleted
        result['ResourceId'] = self.resource_id
        result['ResourceName'] = self.resource_name
        result['ResourceStatus'] = self.resource_status
        result['ResourceType'] = self.resource_type
        result['Tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.region = map.get('Region')
        self.resource_creation_time = map.get('ResourceCreationTime')
        self.resource_deleted = map.get('ResourceDeleted')
        self.resource_id = map.get('ResourceId')
        self.resource_name = map.get('ResourceName')
        self.resource_status = map.get('ResourceStatus')
        self.resource_type = map.get('ResourceType')
        self.tags = map.get('Tags')
        return self


class ListDiscoveredResourcesResponseDiscoveredResourceProfiles(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, discovered_resource_profile_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.discovered_resource_profile_list = discovered_resource_profile_list  # type: List[ListDiscoveredResourcesResponseDiscoveredResourceProfilesDiscoveredResourceProfileList]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.discovered_resource_profile_list, 'discovered_resource_profile_list')
        if self.discovered_resource_profile_list:
            for k in self.discovered_resource_profile_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['DiscoveredResourceProfileList'] = []
        if self.discovered_resource_profile_list is not None:
            for k in self.discovered_resource_profile_list:
                result['DiscoveredResourceProfileList'].append(k.to_map() if k else None)
        else:
            result['DiscoveredResourceProfileList'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.discovered_resource_profile_list = []
        if map.get('DiscoveredResourceProfileList') is not None:
            for k in map.get('DiscoveredResourceProfileList'):
                temp_model = ListDiscoveredResourcesResponseDiscoveredResourceProfilesDiscoveredResourceProfileList()
                self.discovered_resource_profile_list.append(temp_model.from_map(k))
        else:
            self.discovered_resource_profile_list = None
        return self


class DescribeConfigurationRecorderRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeConfigurationRecorderResponse(TeaModel):
    def __init__(self, request_id=None, configuration_recorder=None):
        self.request_id = request_id    # type: str
        self.configuration_recorder = configuration_recorder  # type: DescribeConfigurationRecorderResponseConfigurationRecorder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.configuration_recorder, 'configuration_recorder')
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()
        else:
            result['ConfigurationRecorder'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ConfigurationRecorder') is not None:
            temp_model = DescribeConfigurationRecorderResponseConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(map['ConfigurationRecorder'])
        else:
            self.configuration_recorder = None
        return self


class DescribeConfigurationRecorderResponseConfigurationRecorder(TeaModel):
    def __init__(self, account_id=None, configuration_recorder_status=None, organization_master_id=None,
                 organization_enable_status=None, resource_types=None):
        self.account_id = account_id    # type: int
        self.configuration_recorder_status = configuration_recorder_status  # type: str
        self.organization_master_id = organization_master_id  # type: int
        self.organization_enable_status = organization_enable_status  # type: str
        self.resource_types = resource_types  # type: List[str]

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.configuration_recorder_status, 'configuration_recorder_status')
        self.validate_required(self.organization_master_id, 'organization_master_id')
        self.validate_required(self.organization_enable_status, 'organization_enable_status')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['ConfigurationRecorderStatus'] = self.configuration_recorder_status
        result['OrganizationMasterId'] = self.organization_master_id
        result['OrganizationEnableStatus'] = self.organization_enable_status
        result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.configuration_recorder_status = map.get('ConfigurationRecorderStatus')
        self.organization_master_id = map.get('OrganizationMasterId')
        self.organization_enable_status = map.get('OrganizationEnableStatus')
        self.resource_types = map.get('ResourceTypes')
        return self


class DescribeDiscoveredResourceRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, region=None, multi_account=None, member_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.region = region            # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['Region'] = self.region
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.region = map.get('Region')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class DescribeDiscoveredResourceResponse(TeaModel):
    def __init__(self, request_id=None, discovered_resource_detail=None):
        self.request_id = request_id    # type: str
        self.discovered_resource_detail = discovered_resource_detail  # type: DescribeDiscoveredResourceResponseDiscoveredResourceDetail

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.discovered_resource_detail, 'discovered_resource_detail')
        if self.discovered_resource_detail:
            self.discovered_resource_detail.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.discovered_resource_detail is not None:
            result['DiscoveredResourceDetail'] = self.discovered_resource_detail.to_map()
        else:
            result['DiscoveredResourceDetail'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DiscoveredResourceDetail') is not None:
            temp_model = DescribeDiscoveredResourceResponseDiscoveredResourceDetail()
            self.discovered_resource_detail = temp_model.from_map(map['DiscoveredResourceDetail'])
        else:
            self.discovered_resource_detail = None
        return self


class DescribeDiscoveredResourceResponseDiscoveredResourceDetail(TeaModel):
    def __init__(self, account_id=None, resource_id=None, resource_type=None, resource_name=None, region=None,
                 availability_zone=None, resource_creation_time=None, resource_status=None, resource_deleted=None, tags=None,
                 configuration=None):
        self.account_id = account_id    # type: int
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_name = resource_name  # type: str
        self.region = region            # type: str
        self.availability_zone = availability_zone  # type: str
        self.resource_creation_time = resource_creation_time  # type: int
        self.resource_status = resource_status  # type: str
        self.resource_deleted = resource_deleted  # type: int
        self.tags = tags                # type: str
        self.configuration = configuration  # type: str

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.region, 'region')
        self.validate_required(self.availability_zone, 'availability_zone')
        self.validate_required(self.resource_creation_time, 'resource_creation_time')
        self.validate_required(self.resource_status, 'resource_status')
        self.validate_required(self.resource_deleted, 'resource_deleted')
        self.validate_required(self.tags, 'tags')
        self.validate_required(self.configuration, 'configuration')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['ResourceName'] = self.resource_name
        result['Region'] = self.region
        result['AvailabilityZone'] = self.availability_zone
        result['ResourceCreationTime'] = self.resource_creation_time
        result['ResourceStatus'] = self.resource_status
        result['ResourceDeleted'] = self.resource_deleted
        result['Tags'] = self.tags
        result['Configuration'] = self.configuration
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.resource_name = map.get('ResourceName')
        self.region = map.get('Region')
        self.availability_zone = map.get('AvailabilityZone')
        self.resource_creation_time = map.get('ResourceCreationTime')
        self.resource_status = map.get('ResourceStatus')
        self.resource_deleted = map.get('ResourceDeleted')
        self.tags = map.get('Tags')
        self.configuration = map.get('Configuration')
        return self


class StartConfigurationRecorderRequest(TeaModel):
    def __init__(self, enterprise_edition=None):
        self.enterprise_edition = enterprise_edition  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['EnterpriseEdition'] = self.enterprise_edition
        return result

    def from_map(self, map={}):
        self.enterprise_edition = map.get('EnterpriseEdition')
        return self


class StartConfigurationRecorderResponse(TeaModel):
    def __init__(self, request_id=None, configuration_recorder=None):
        self.request_id = request_id    # type: str
        self.configuration_recorder = configuration_recorder  # type: StartConfigurationRecorderResponseConfigurationRecorder

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.configuration_recorder, 'configuration_recorder')
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()
        else:
            result['ConfigurationRecorder'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ConfigurationRecorder') is not None:
            temp_model = StartConfigurationRecorderResponseConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(map['ConfigurationRecorder'])
        else:
            self.configuration_recorder = None
        return self


class StartConfigurationRecorderResponseConfigurationRecorder(TeaModel):
    def __init__(self, account_id=None, configuration_recorder_status=None, organization_master_id=None,
                 organization_enable_status=None, resource_types=None):
        self.account_id = account_id    # type: int
        self.configuration_recorder_status = configuration_recorder_status  # type: str
        self.organization_master_id = organization_master_id  # type: int
        self.organization_enable_status = organization_enable_status  # type: str
        self.resource_types = resource_types  # type: List[str]

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.configuration_recorder_status, 'configuration_recorder_status')
        self.validate_required(self.organization_master_id, 'organization_master_id')
        self.validate_required(self.organization_enable_status, 'organization_enable_status')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = {}
        result['AccountId'] = self.account_id
        result['ConfigurationRecorderStatus'] = self.configuration_recorder_status
        result['OrganizationMasterId'] = self.organization_master_id
        result['OrganizationEnableStatus'] = self.organization_enable_status
        result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        self.account_id = map.get('AccountId')
        self.configuration_recorder_status = map.get('ConfigurationRecorderStatus')
        self.organization_master_id = map.get('OrganizationMasterId')
        self.organization_enable_status = map.get('OrganizationEnableStatus')
        self.resource_types = map.get('ResourceTypes')
        return self


class DescribeConfigRuleRequest(TeaModel):
    def __init__(self, config_rule_id=None, multi_account=None, member_id=None):
        self.config_rule_id = config_rule_id  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        self.validate_required(self.config_rule_id, 'config_rule_id')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class DescribeConfigRuleResponse(TeaModel):
    def __init__(self, request_id=None, config_rule=None):
        self.request_id = request_id    # type: str
        self.config_rule = config_rule  # type: DescribeConfigRuleResponseConfigRule

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.config_rule, 'config_rule')
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()
        else:
            result['ConfigRule'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ConfigRule') is not None:
            temp_model = DescribeConfigRuleResponseConfigRule()
            self.config_rule = temp_model.from_map(map['ConfigRule'])
        else:
            self.config_rule = None
        return self


class DescribeConfigRuleResponseConfigRuleCreateBy(TeaModel):
    def __init__(self, creator_type=None, creator_id=None, creator_name=None, config_rule_scene_id=None,
                 config_rule_scene_name=None):
        self.creator_type = creator_type  # type: str
        self.creator_id = creator_id    # type: str
        self.creator_name = creator_name  # type: str
        self.config_rule_scene_id = config_rule_scene_id  # type: str
        self.config_rule_scene_name = config_rule_scene_name  # type: str

    def validate(self):
        self.validate_required(self.creator_type, 'creator_type')
        self.validate_required(self.creator_id, 'creator_id')
        self.validate_required(self.creator_name, 'creator_name')
        self.validate_required(self.config_rule_scene_id, 'config_rule_scene_id')
        self.validate_required(self.config_rule_scene_name, 'config_rule_scene_name')

    def to_map(self):
        result = {}
        result['CreatorType'] = self.creator_type
        result['CreatorId'] = self.creator_id
        result['CreatorName'] = self.creator_name
        result['ConfigRuleSceneId'] = self.config_rule_scene_id
        result['ConfigRuleSceneName'] = self.config_rule_scene_name
        return result

    def from_map(self, map={}):
        self.creator_type = map.get('CreatorType')
        self.creator_id = map.get('CreatorId')
        self.creator_name = map.get('CreatorName')
        self.config_rule_scene_id = map.get('ConfigRuleSceneId')
        self.config_rule_scene_name = map.get('ConfigRuleSceneName')
        return self


class DescribeConfigRuleResponseConfigRuleConfigRuleEvaluationStatus(TeaModel):
    def __init__(self, first_activated_timestamp=None, first_evaluation_started=None, last_error_code=None,
                 last_error_message=None, last_failed_evaluation_timestamp=None, last_failed_invocation_timestamp=None,
                 last_successful_evaluation_timestamp=None, last_successful_invocation_timestamp=None):
        self.first_activated_timestamp = first_activated_timestamp  # type: int
        self.first_evaluation_started = first_evaluation_started  # type: bool
        self.last_error_code = last_error_code  # type: str
        self.last_error_message = last_error_message  # type: str
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp  # type: int
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp  # type: int
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp  # type: int
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp  # type: int

    def validate(self):
        self.validate_required(self.first_activated_timestamp, 'first_activated_timestamp')
        self.validate_required(self.first_evaluation_started, 'first_evaluation_started')
        self.validate_required(self.last_error_code, 'last_error_code')
        self.validate_required(self.last_error_message, 'last_error_message')
        self.validate_required(self.last_failed_evaluation_timestamp, 'last_failed_evaluation_timestamp')
        self.validate_required(self.last_failed_invocation_timestamp, 'last_failed_invocation_timestamp')
        self.validate_required(self.last_successful_evaluation_timestamp, 'last_successful_evaluation_timestamp')
        self.validate_required(self.last_successful_invocation_timestamp, 'last_successful_invocation_timestamp')

    def to_map(self):
        result = {}
        result['FirstActivatedTimestamp'] = self.first_activated_timestamp
        result['FirstEvaluationStarted'] = self.first_evaluation_started
        result['LastErrorCode'] = self.last_error_code
        result['LastErrorMessage'] = self.last_error_message
        result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp
        result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp
        result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp
        result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp
        return result

    def from_map(self, map={}):
        self.first_activated_timestamp = map.get('FirstActivatedTimestamp')
        self.first_evaluation_started = map.get('FirstEvaluationStarted')
        self.last_error_code = map.get('LastErrorCode')
        self.last_error_message = map.get('LastErrorMessage')
        self.last_failed_evaluation_timestamp = map.get('LastFailedEvaluationTimestamp')
        self.last_failed_invocation_timestamp = map.get('LastFailedInvocationTimestamp')
        self.last_successful_evaluation_timestamp = map.get('LastSuccessfulEvaluationTimestamp')
        self.last_successful_invocation_timestamp = map.get('LastSuccessfulInvocationTimestamp')
        return self


class DescribeConfigRuleResponseConfigRuleManagedRuleSourceDetails(TeaModel):
    def __init__(self, event_source=None, maximum_execution_frequency=None, message_type=None):
        self.event_source = event_source  # type: str
        self.maximum_execution_frequency = maximum_execution_frequency  # type: str
        self.message_type = message_type  # type: str

    def validate(self):
        self.validate_required(self.event_source, 'event_source')
        self.validate_required(self.maximum_execution_frequency, 'maximum_execution_frequency')
        self.validate_required(self.message_type, 'message_type')

    def to_map(self):
        result = {}
        result['EventSource'] = self.event_source
        result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        result['MessageType'] = self.message_type
        return result

    def from_map(self, map={}):
        self.event_source = map.get('EventSource')
        self.maximum_execution_frequency = map.get('MaximumExecutionFrequency')
        self.message_type = map.get('MessageType')
        return self


class DescribeConfigRuleResponseConfigRuleManagedRule(TeaModel):
    def __init__(self, managed_rule_name=None, description=None, identifier=None,
                 compulsory_input_parameter_details=None, optional_input_parameter_details=None, help_url=None, source_details=None, labels=None):
        self.managed_rule_name = managed_rule_name  # type: str
        self.description = description  # type: str
        self.identifier = identifier    # type: str
        self.compulsory_input_parameter_details = compulsory_input_parameter_details  # type: Dict[str, Any]
        self.optional_input_parameter_details = optional_input_parameter_details  # type: Dict[str, Any]
        self.help_url = help_url        # type: str
        self.source_details = source_details  # type: List[DescribeConfigRuleResponseConfigRuleManagedRuleSourceDetails]
        self.labels = labels            # type: List[str]

    def validate(self):
        self.validate_required(self.managed_rule_name, 'managed_rule_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.identifier, 'identifier')
        self.validate_required(self.compulsory_input_parameter_details, 'compulsory_input_parameter_details')
        self.validate_required(self.optional_input_parameter_details, 'optional_input_parameter_details')
        self.validate_required(self.help_url, 'help_url')
        self.validate_required(self.source_details, 'source_details')
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()
        self.validate_required(self.labels, 'labels')

    def to_map(self):
        result = {}
        result['ManagedRuleName'] = self.managed_rule_name
        result['Description'] = self.description
        result['Identifier'] = self.identifier
        result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details
        result['OptionalInputParameterDetails'] = self.optional_input_parameter_details
        result['HelpUrl'] = self.help_url
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        else:
            result['SourceDetails'] = None
        result['Labels'] = self.labels
        return result

    def from_map(self, map={}):
        self.managed_rule_name = map.get('ManagedRuleName')
        self.description = map.get('Description')
        self.identifier = map.get('Identifier')
        self.compulsory_input_parameter_details = map.get('CompulsoryInputParameterDetails')
        self.optional_input_parameter_details = map.get('OptionalInputParameterDetails')
        self.help_url = map.get('HelpUrl')
        self.source_details = []
        if map.get('SourceDetails') is not None:
            for k in map.get('SourceDetails'):
                temp_model = DescribeConfigRuleResponseConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        else:
            self.source_details = None
        self.labels = map.get('Labels')
        return self


class DescribeConfigRuleResponseConfigRuleSourceSourceConditions(TeaModel):
    def __init__(self, desired_value=None, name=None, operator=None, required=None, select_path=None, tips=None):
        self.desired_value = desired_value  # type: str
        self.name = name                # type: str
        self.operator = operator        # type: str
        self.required = required        # type: bool
        self.select_path = select_path  # type: str
        self.tips = tips                # type: str

    def validate(self):
        self.validate_required(self.desired_value, 'desired_value')
        self.validate_required(self.name, 'name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.required, 'required')
        self.validate_required(self.select_path, 'select_path')
        self.validate_required(self.tips, 'tips')

    def to_map(self):
        result = {}
        result['DesiredValue'] = self.desired_value
        result['Name'] = self.name
        result['Operator'] = self.operator
        result['Required'] = self.required
        result['SelectPath'] = self.select_path
        result['Tips'] = self.tips
        return result

    def from_map(self, map={}):
        self.desired_value = map.get('DesiredValue')
        self.name = map.get('Name')
        self.operator = map.get('Operator')
        self.required = map.get('Required')
        self.select_path = map.get('SelectPath')
        self.tips = map.get('Tips')
        return self


class DescribeConfigRuleResponseConfigRuleSourceSourceDetails(TeaModel):
    def __init__(self, event_source=None, maximum_execution_frequency=None, message_type=None):
        self.event_source = event_source  # type: str
        self.maximum_execution_frequency = maximum_execution_frequency  # type: str
        self.message_type = message_type  # type: str

    def validate(self):
        self.validate_required(self.event_source, 'event_source')
        self.validate_required(self.maximum_execution_frequency, 'maximum_execution_frequency')
        self.validate_required(self.message_type, 'message_type')

    def to_map(self):
        result = {}
        result['EventSource'] = self.event_source
        result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        result['MessageType'] = self.message_type
        return result

    def from_map(self, map={}):
        self.event_source = map.get('EventSource')
        self.maximum_execution_frequency = map.get('MaximumExecutionFrequency')
        self.message_type = map.get('MessageType')
        return self


class DescribeConfigRuleResponseConfigRuleSource(TeaModel):
    def __init__(self, identifier=None, owner=None, source_conditions=None, source_details=None):
        self.identifier = identifier    # type: str
        self.owner = owner              # type: str
        self.source_conditions = source_conditions  # type: List[DescribeConfigRuleResponseConfigRuleSourceSourceConditions]
        self.source_details = source_details  # type: List[DescribeConfigRuleResponseConfigRuleSourceSourceDetails]

    def validate(self):
        self.validate_required(self.identifier, 'identifier')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.source_conditions, 'source_conditions')
        if self.source_conditions:
            for k in self.source_conditions:
                if k:
                    k.validate()
        self.validate_required(self.source_details, 'source_details')
        if self.source_details:
            for k in self.source_details:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Identifier'] = self.identifier
        result['Owner'] = self.owner
        result['SourceConditions'] = []
        if self.source_conditions is not None:
            for k in self.source_conditions:
                result['SourceConditions'].append(k.to_map() if k else None)
        else:
            result['SourceConditions'] = None
        result['SourceDetails'] = []
        if self.source_details is not None:
            for k in self.source_details:
                result['SourceDetails'].append(k.to_map() if k else None)
        else:
            result['SourceDetails'] = None
        return result

    def from_map(self, map={}):
        self.identifier = map.get('Identifier')
        self.owner = map.get('Owner')
        self.source_conditions = []
        if map.get('SourceConditions') is not None:
            for k in map.get('SourceConditions'):
                temp_model = DescribeConfigRuleResponseConfigRuleSourceSourceConditions()
                self.source_conditions.append(temp_model.from_map(k))
        else:
            self.source_conditions = None
        self.source_details = []
        if map.get('SourceDetails') is not None:
            for k in map.get('SourceDetails'):
                temp_model = DescribeConfigRuleResponseConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k))
        else:
            self.source_details = None
        return self


class DescribeConfigRuleResponseConfigRuleScope(TeaModel):
    def __init__(self, compliance_resource_id=None, compliance_resource_types=None):
        self.compliance_resource_id = compliance_resource_id  # type: str
        self.compliance_resource_types = compliance_resource_types  # type: List[str]

    def validate(self):
        self.validate_required(self.compliance_resource_id, 'compliance_resource_id')
        self.validate_required(self.compliance_resource_types, 'compliance_resource_types')

    def to_map(self):
        result = {}
        result['ComplianceResourceId'] = self.compliance_resource_id
        result['ComplianceResourceTypes'] = self.compliance_resource_types
        return result

    def from_map(self, map={}):
        self.compliance_resource_id = map.get('ComplianceResourceId')
        self.compliance_resource_types = map.get('ComplianceResourceTypes')
        return self


class DescribeConfigRuleResponseConfigRule(TeaModel):
    def __init__(self, config_rule_arn=None, config_rule_id=None, config_rule_name=None, config_rule_state=None,
                 create_timestamp=None, description=None, input_parameters=None, modified_timestamp=None, risk_level=None,
                 maximum_execution_frequency=None, create_by=None, config_rule_evaluation_status=None, managed_rule=None, source=None,
                 scope=None):
        self.config_rule_arn = config_rule_arn  # type: str
        self.config_rule_id = config_rule_id  # type: str
        self.config_rule_name = config_rule_name  # type: str
        self.config_rule_state = config_rule_state  # type: str
        self.create_timestamp = create_timestamp  # type: int
        self.description = description  # type: str
        self.input_parameters = input_parameters  # type: Dict[str, Any]
        self.modified_timestamp = modified_timestamp  # type: int
        self.risk_level = risk_level    # type: int
        self.maximum_execution_frequency = maximum_execution_frequency  # type: str
        self.create_by = create_by      # type: DescribeConfigRuleResponseConfigRuleCreateBy
        self.config_rule_evaluation_status = config_rule_evaluation_status  # type: DescribeConfigRuleResponseConfigRuleConfigRuleEvaluationStatus
        self.managed_rule = managed_rule  # type: DescribeConfigRuleResponseConfigRuleManagedRule
        self.source = source            # type: DescribeConfigRuleResponseConfigRuleSource
        self.scope = scope              # type: DescribeConfigRuleResponseConfigRuleScope

    def validate(self):
        self.validate_required(self.config_rule_arn, 'config_rule_arn')
        self.validate_required(self.config_rule_id, 'config_rule_id')
        self.validate_required(self.config_rule_name, 'config_rule_name')
        self.validate_required(self.config_rule_state, 'config_rule_state')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.description, 'description')
        self.validate_required(self.input_parameters, 'input_parameters')
        self.validate_required(self.modified_timestamp, 'modified_timestamp')
        self.validate_required(self.risk_level, 'risk_level')
        self.validate_required(self.maximum_execution_frequency, 'maximum_execution_frequency')
        self.validate_required(self.create_by, 'create_by')
        if self.create_by:
            self.create_by.validate()
        self.validate_required(self.config_rule_evaluation_status, 'config_rule_evaluation_status')
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()
        self.validate_required(self.managed_rule, 'managed_rule')
        if self.managed_rule:
            self.managed_rule.validate()
        self.validate_required(self.source, 'source')
        if self.source:
            self.source.validate()
        self.validate_required(self.scope, 'scope')
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = {}
        result['ConfigRuleArn'] = self.config_rule_arn
        result['ConfigRuleId'] = self.config_rule_id
        result['ConfigRuleName'] = self.config_rule_name
        result['ConfigRuleState'] = self.config_rule_state
        result['CreateTimestamp'] = self.create_timestamp
        result['Description'] = self.description
        result['InputParameters'] = self.input_parameters
        result['ModifiedTimestamp'] = self.modified_timestamp
        result['RiskLevel'] = self.risk_level
        result['MaximumExecutionFrequency'] = self.maximum_execution_frequency
        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()
        else:
            result['CreateBy'] = None
        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()
        else:
            result['ConfigRuleEvaluationStatus'] = None
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()
        else:
            result['ManagedRule'] = None
        if self.source is not None:
            result['Source'] = self.source.to_map()
        else:
            result['Source'] = None
        if self.scope is not None:
            result['Scope'] = self.scope.to_map()
        else:
            result['Scope'] = None
        return result

    def from_map(self, map={}):
        self.config_rule_arn = map.get('ConfigRuleArn')
        self.config_rule_id = map.get('ConfigRuleId')
        self.config_rule_name = map.get('ConfigRuleName')
        self.config_rule_state = map.get('ConfigRuleState')
        self.create_timestamp = map.get('CreateTimestamp')
        self.description = map.get('Description')
        self.input_parameters = map.get('InputParameters')
        self.modified_timestamp = map.get('ModifiedTimestamp')
        self.risk_level = map.get('RiskLevel')
        self.maximum_execution_frequency = map.get('MaximumExecutionFrequency')
        if map.get('CreateBy') is not None:
            temp_model = DescribeConfigRuleResponseConfigRuleCreateBy()
            self.create_by = temp_model.from_map(map['CreateBy'])
        else:
            self.create_by = None
        if map.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = DescribeConfigRuleResponseConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(map['ConfigRuleEvaluationStatus'])
        else:
            self.config_rule_evaluation_status = None
        if map.get('ManagedRule') is not None:
            temp_model = DescribeConfigRuleResponseConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(map['ManagedRule'])
        else:
            self.managed_rule = None
        if map.get('Source') is not None:
            temp_model = DescribeConfigRuleResponseConfigRuleSource()
            self.source = temp_model.from_map(map['Source'])
        else:
            self.source = None
        if map.get('Scope') is not None:
            temp_model = DescribeConfigRuleResponseConfigRuleScope()
            self.scope = temp_model.from_map(map['Scope'])
        else:
            self.scope = None
        return self


class GetSupportedResourceTypesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetSupportedResourceTypesResponse(TeaModel):
    def __init__(self, request_id=None, resource_types=None):
        self.request_id = request_id    # type: str
        self.resource_types = resource_types  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.resource_types = map.get('ResourceTypes')
        return self


class PutDeliveryChannelRequest(TeaModel):
    def __init__(self, client_token=None, delivery_channel_id=None, delivery_channel_name=None,
                 delivery_channel_type=None, delivery_channel_target_arn=None, delivery_channel_assume_role_arn=None,
                 delivery_channel_condition=None, description=None, status=None):
        self.client_token = client_token  # type: str
        self.delivery_channel_id = delivery_channel_id  # type: str
        self.delivery_channel_name = delivery_channel_name  # type: str
        self.delivery_channel_type = delivery_channel_type  # type: str
        self.delivery_channel_target_arn = delivery_channel_target_arn  # type: str
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn  # type: str
        self.delivery_channel_condition = delivery_channel_condition  # type: str
        self.description = description  # type: str
        self.status = status            # type: int

    def validate(self):
        self.validate_required(self.delivery_channel_type, 'delivery_channel_type')
        self.validate_required(self.delivery_channel_target_arn, 'delivery_channel_target_arn')
        self.validate_required(self.delivery_channel_assume_role_arn, 'delivery_channel_assume_role_arn')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DeliveryChannelId'] = self.delivery_channel_id
        result['DeliveryChannelName'] = self.delivery_channel_name
        result['DeliveryChannelType'] = self.delivery_channel_type
        result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn
        result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn
        result['DeliveryChannelCondition'] = self.delivery_channel_condition
        result['Description'] = self.description
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.delivery_channel_id = map.get('DeliveryChannelId')
        self.delivery_channel_name = map.get('DeliveryChannelName')
        self.delivery_channel_type = map.get('DeliveryChannelType')
        self.delivery_channel_target_arn = map.get('DeliveryChannelTargetArn')
        self.delivery_channel_assume_role_arn = map.get('DeliveryChannelAssumeRoleArn')
        self.delivery_channel_condition = map.get('DeliveryChannelCondition')
        self.description = map.get('Description')
        self.status = map.get('Status')
        return self


class PutDeliveryChannelResponse(TeaModel):
    def __init__(self, request_id=None, delivery_channel_id=None):
        self.request_id = request_id    # type: str
        self.delivery_channel_id = delivery_channel_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.delivery_channel_id, 'delivery_channel_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.delivery_channel_id = map.get('DeliveryChannelId')
        return self


class PutEvaluationsRequest(TeaModel):
    def __init__(self, result_token=None, evaluations=None):
        self.result_token = result_token  # type: str
        self.evaluations = evaluations  # type: str

    def validate(self):
        self.validate_required(self.result_token, 'result_token')

    def to_map(self):
        result = {}
        result['ResultToken'] = self.result_token
        result['Evaluations'] = self.evaluations
        return result

    def from_map(self, map={}):
        self.result_token = map.get('ResultToken')
        self.evaluations = map.get('Evaluations')
        return self


class PutEvaluationsResponse(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id    # type: str
        self.result = result            # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Result'] = self.result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.result = map.get('Result')
        return self


class StartConfigRuleEvaluationRequest(TeaModel):
    def __init__(self, config_rule_id=None, multi_account=None, member_id=None):
        self.config_rule_id = config_rule_id  # type: str
        self.multi_account = multi_account  # type: bool
        self.member_id = member_id      # type: int

    def validate(self):
        self.validate_required(self.config_rule_id, 'config_rule_id')

    def to_map(self):
        result = {}
        result['ConfigRuleId'] = self.config_rule_id
        result['MultiAccount'] = self.multi_account
        result['MemberId'] = self.member_id
        return result

    def from_map(self, map={}):
        self.config_rule_id = map.get('ConfigRuleId')
        self.multi_account = map.get('MultiAccount')
        self.member_id = map.get('MemberId')
        return self


class StartConfigRuleEvaluationResponse(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id    # type: str
        self.result = result            # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Result'] = self.result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.result = map.get('Result')
        return self
