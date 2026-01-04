# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVpcPublishedRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        route_entries: List[main_models.ListVpcPublishedRouteEntriesResponseBodyRouteEntries] = None,
    ):
        # Indicates whether there is a token for the next query. Values:
        # 
        # - If **NextToken** is empty, it means there is no next query.
        # - If **NextToken** has a return value, this value indicates the token for the start of the next query.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # List of route entry publishing status information.
        self.route_entries = route_entries

    def validate(self):
        if self.route_entries:
            for v1 in self.route_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteEntries'] = []
        if self.route_entries is not None:
            for k1 in self.route_entries:
                result['RouteEntries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_entries = []
        if m.get('RouteEntries') is not None:
            for k1 in m.get('RouteEntries'):
                temp_model = main_models.ListVpcPublishedRouteEntriesResponseBodyRouteEntries()
                self.route_entries.append(temp_model.from_map(k1))

        return self

class ListVpcPublishedRouteEntriesResponseBodyRouteEntries(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        route_entry_id: str = None,
        route_publish_targets: List[main_models.ListVpcPublishedRouteEntriesResponseBodyRouteEntriesRoutePublishTargets] = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the route entry.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the route entry.
        self.route_entry_id = route_entry_id
        # List of route entry publishing status information in the publishing targets.
        self.route_publish_targets = route_publish_targets
        # The ID of the route table.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_publish_targets:
            for v1 in self.route_publish_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        result['RoutePublishTargets'] = []
        if self.route_publish_targets is not None:
            for k1 in self.route_publish_targets:
                result['RoutePublishTargets'].append(k1.to_map() if k1 else None)

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        self.route_publish_targets = []
        if m.get('RoutePublishTargets') is not None:
            for k1 in m.get('RoutePublishTargets'):
                temp_model = main_models.ListVpcPublishedRouteEntriesResponseBodyRouteEntriesRoutePublishTargets()
                self.route_publish_targets.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class ListVpcPublishedRouteEntriesResponseBodyRouteEntriesRoutePublishTargets(DaraModel):
    def __init__(
        self,
        publish_status: str = None,
        publish_target_instance_id: str = None,
        publish_target_type: str = None,
    ):
        # The publishing status of the route entry in the publishing target.
        self.publish_status = publish_status
        # The ID of the route publishing target instance.
        self.publish_target_instance_id = publish_target_instance_id
        # The type of the route publishing target.
        self.publish_target_type = publish_target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.publish_target_instance_id is not None:
            result['PublishTargetInstanceId'] = self.publish_target_instance_id

        if self.publish_target_type is not None:
            result['PublishTargetType'] = self.publish_target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('PublishTargetInstanceId') is not None:
            self.publish_target_instance_id = m.get('PublishTargetInstanceId')

        if m.get('PublishTargetType') is not None:
            self.publish_target_type = m.get('PublishTargetType')

        return self

