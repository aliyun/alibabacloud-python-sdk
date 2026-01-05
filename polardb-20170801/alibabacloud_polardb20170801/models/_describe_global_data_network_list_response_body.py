# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalDataNetworkListResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeGlobalDataNetworkListResponseBodyItems = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeGlobalDataNetworkListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGlobalDataNetworkListResponseBodyItems(DaraModel):
    def __init__(
        self,
        networks: List[main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworks] = None,
    ):
        self.networks = networks

    def validate(self):
        if self.networks:
            for v1 in self.networks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Networks'] = []
        if self.networks is not None:
            for k1 in self.networks:
                result['Networks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.networks = []
        if m.get('Networks') is not None:
            for k1 in m.get('Networks'):
                temp_model = main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworks()
                self.networks.append(temp_model.from_map(k1))

        return self

class DescribeGlobalDataNetworkListResponseBodyItemsNetworks(DaraModel):
    def __init__(
        self,
        channels: List[main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksChannels] = None,
        create_time: str = None,
        network_description: str = None,
        network_id: str = None,
        network_status: str = None,
        network_topology: main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopology = None,
    ):
        self.channels = channels
        self.create_time = create_time
        self.network_description = network_description
        # GDN ID
        self.network_id = network_id
        self.network_status = network_status
        self.network_topology = network_topology

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()
        if self.network_topology:
            self.network_topology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['Channels'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.network_description is not None:
            result['NetworkDescription'] = self.network_description

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_status is not None:
            result['NetworkStatus'] = self.network_status

        if self.network_topology is not None:
            result['NetworkTopology'] = self.network_topology.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k1 in m.get('Channels'):
                temp_model = main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NetworkDescription') is not None:
            self.network_description = m.get('NetworkDescription')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkStatus') is not None:
            self.network_status = m.get('NetworkStatus')

        if m.get('NetworkTopology') is not None:
            temp_model = main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopology()
            self.network_topology = temp_model.from_map(m.get('NetworkTopology'))

        return self

class DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopology(DaraModel):
    def __init__(
        self,
        destinations: List[main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopologyDestinations] = None,
        sources: List[main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopologySources] = None,
    ):
        self.destinations = destinations
        self.sources = sources

    def validate(self):
        if self.destinations:
            for v1 in self.destinations:
                 if v1:
                    v1.validate()
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Destinations'] = []
        if self.destinations is not None:
            for k1 in self.destinations:
                result['Destinations'].append(k1.to_map() if k1 else None)

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.destinations = []
        if m.get('Destinations') is not None:
            for k1 in m.get('Destinations'):
                temp_model = main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopologyDestinations()
                self.destinations.append(temp_model.from_map(k1))

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopologySources()
                self.sources.append(temp_model.from_map(k1))

        return self

class DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopologySources(DaraModel):
    def __init__(
        self,
        source_file_system_path: str = None,
        source_id: str = None,
        source_region: str = None,
        source_type: str = None,
    ):
        self.source_file_system_path = source_file_system_path
        self.source_id = source_id
        self.source_region = source_region
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_file_system_path is not None:
            result['SourceFileSystemPath'] = self.source_file_system_path

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceFileSystemPath') is not None:
            self.source_file_system_path = m.get('SourceFileSystemPath')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribeGlobalDataNetworkListResponseBodyItemsNetworksNetworkTopologyDestinations(DaraModel):
    def __init__(
        self,
        destination_file_system_path: str = None,
        destination_id: str = None,
        destination_region: str = None,
        destination_type: str = None,
    ):
        self.destination_file_system_path = destination_file_system_path
        self.destination_id = destination_id
        self.destination_region = destination_region
        self.destination_type = destination_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_file_system_path is not None:
            result['DestinationFileSystemPath'] = self.destination_file_system_path

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationFileSystemPath') is not None:
            self.destination_file_system_path = m.get('DestinationFileSystemPath')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        return self

class DescribeGlobalDataNetworkListResponseBodyItemsNetworksChannels(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        channel_status: str = None,
        freeze_source_during_sync: bool = None,
        progress: str = None,
    ):
        self.channel_id = channel_id
        self.channel_status = channel_status
        self.freeze_source_during_sync = freeze_source_during_sync
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_status is not None:
            result['ChannelStatus'] = self.channel_status

        if self.freeze_source_during_sync is not None:
            result['FreezeSourceDuringSync'] = self.freeze_source_during_sync

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelStatus') is not None:
            self.channel_status = m.get('ChannelStatus')

        if m.get('FreezeSourceDuringSync') is not None:
            self.freeze_source_during_sync = m.get('FreezeSourceDuringSync')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

