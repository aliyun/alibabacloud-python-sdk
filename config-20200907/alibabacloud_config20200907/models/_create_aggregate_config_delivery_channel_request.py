# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAggregateConfigDeliveryChannelRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliant_snapshot: bool = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # A client-generated token that you can use to ensure the idempotence of the request. You must make sure that the token is unique for each request.
        # 
        # The `ClientToken` parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to deliver compliance snapshots. Cloud Config delivers information about the compliance and non-compliance of resources to SLS. Valid values:
        # 
        # - true: Deliver compliance snapshots.
        # 
        # - false: Do not deliver compliance snapshots.
        self.compliant_snapshot = compliant_snapshot
        # Specifies whether to deliver the resource configuration change history. If the configurations of a resource change, Cloud Config delivers the configuration change history to OSS, SLS, or MNS. Valid values:
        # 
        # - true: Deliver the resource configuration change history.
        # 
        # - false (default): Do not deliver the resource configuration change history.
        # 
        # > * If the delivery channel type is OSS, you must set at least one of the \\`ConfigurationSnapshot\\` and \\`ConfigurationItemChangeNotification\\` parameters to true.
        # 
        # > - If the delivery channel type is SLS, you must set at least one of the \\`ConfigurationSnapshot\\`, \\`ConfigurationItemChangeNotification\\`, and \\`NonCompliantNotification\\` parameters to true.
        # 
        # > - If the delivery channel type is MNS, you must set at least one of the \\`ConfigurationItemChangeNotification\\` and \\`NonCompliantNotification\\` parameters to true.
        self.configuration_item_change_notification = configuration_item_change_notification
        # Specifies whether to deliver scheduled resource snapshots. Cloud Config delivers scheduled resource snapshots to OSS, SLS, or MNS at `04:00Z` and `16:00Z` (UTC) every day. Valid values:
        # 
        # - true: Deliver scheduled resource snapshots.
        # 
        # - false (default): Do not deliver scheduled resource snapshots.
        # 
        # > * If the delivery channel type is OSS, you must set at least one of the \\`ConfigurationSnapshot\\` and \\`ConfigurationItemChangeNotification\\` parameters to true.
        # 
        # > - If the delivery channel type is SLS, you must set at least one of the \\`ConfigurationSnapshot\\`, \\`ConfigurationItemChangeNotification\\`, and \\`NonCompliantNotification\\` parameters to true.
        self.configuration_snapshot = configuration_snapshot
        # The rule that is used to filter events or resources for the delivery channel. This parameter is supported for all deliveries to MNS channels and for snapshot deliveries to SLS channels.
        # 
        # - For an MNS channel, you can specify the following rules to filter events:
        # 
        #   - The minimum risk level of the events to which you want to subscribe is `{"filterType":"RuleRiskLevel","value":"1","multiple":false}`.
        # 
        #     The \\`value\\` parameter specifies the risk level. Valid values: 1, 2, and 3. The value 1 indicates high risk. The value 2 indicates medium risk. The value 3 indicates low risk.
        # 
        #   - The resource types of the events to which you want to subscribe are `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #     The \\`values\\` parameter specifies the resource types of the events to which you want to subscribe. The value of this parameter is a JSON array of strings.
        #     Example:
        #     `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        # 
        # - For an SLS channel, you can specify the following rule to filter snapshots:
        # 
        #   The resource types of the snapshots to be delivered are `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #   `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        self.delivery_channel_condition = delivery_channel_condition
        # The name of the delivery channel.
        # 
        # > If you do not set this parameter, this parameter is empty.
        self.delivery_channel_name = delivery_channel_name
        # The ARN of the delivery destination. Valid values:
        # 
        # - If the delivery channel type is OSS, the value of this parameter is in the `acs:oss:{RegionId}:{accountId}:{bucketName}` format. Example: `acs:oss:cn-shanghai:100931896542****:new-bucket`.
        # 
        # - If the delivery channel type is MNS, the value of this parameter is in the `acs:mns:{RegionId}:{accountId}:/topics/{topicName}` format. Example: `acs:mns:cn-shanghai:100931896542****:/topics/topic1`.
        # 
        # - If the delivery channel type is SLS, the value of this parameter is in the `acs:log:{RegionId}:{accountId}:project/{projectName}/logstore/{logstoreName}` format. Example: `acs:log:cn-shanghai:100931896542****:project/project1/logstore/logstore1`.
        # 
        # This parameter is required.
        self.delivery_channel_target_arn = delivery_channel_target_arn
        # The type of the delivery channel. Valid values:
        # 
        # - OSS: Object Storage Service
        # 
        # - MNS: Simple Message Queue
        # 
        # - SLS: Simple Log Service
        # 
        # This parameter is required.
        self.delivery_channel_type = delivery_channel_type
        # The time of day from which scheduled resource snapshots are delivered. The time is displayed in UTC.
        # 
        # The value is in the `HH:mmZ` format.
        # 
        # > If you enable the scheduled delivery of resource snapshots, you can use this parameter to customize the delivery time. If you do not set this parameter, the snapshots are delivered at `04:00Z` and `16:00Z` every day by default.
        self.delivery_snapshot_time = delivery_snapshot_time
        # The description of the delivery channel.
        self.description = description
        # Specifies whether to deliver resource non-compliance events. If a resource is evaluated as non-compliant, Cloud Config delivers the non-compliance event to SLS or MNS. Valid values:
        # 
        # - true: Deliver resource non-compliance events.
        # 
        # - false (default): Do not deliver resource non-compliance events.
        # 
        # > * If the delivery channel type is SLS, you must set at least one of the \\`ConfigurationSnapshot\\`, \\`ConfigurationItemChangeNotification\\`, and \\`NonCompliantNotification\\` parameters to true.
        # 
        # > - If the delivery channel type is MNS, you must set at least one of the \\`ConfigurationItemChangeNotification\\` and \\`NonCompliantNotification\\` parameters to true.
        self.non_compliant_notification = non_compliant_notification
        # The ARN of the OSS bucket that is used to store oversized data to be delivered when the size of the data exceeds the specified limit of the delivery channel. The value is in the `acs:oss:{RegionId}:{accountId}:{bucketName}` format.
        # 
        # If you do not set this parameter, Cloud Config delivers only summary information.
        # 
        # > This parameter is applicable only to delivery channels of the SLS or MNS type. The maximum size of data that can be delivered to an SLS Logstore is 1 MB. The maximum size of data that can be delivered to an MNS topic is 64 KB.
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compliant_snapshot is not None:
            result['CompliantSnapshot'] = self.compliant_snapshot

        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification

        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot

        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn

        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type

        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time

        if self.description is not None:
            result['Description'] = self.description

        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification

        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompliantSnapshot') is not None:
            self.compliant_snapshot = m.get('CompliantSnapshot')

        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')

        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')

        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')

        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')

        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')

        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')

        return self

