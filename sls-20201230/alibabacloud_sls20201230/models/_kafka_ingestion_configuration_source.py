# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KafkaIngestionConfigurationSource(DaraModel):
    def __init__(
        self,
        bootstrap_servers: str = None,
        communication: str = None,
        consumer_group: str = None,
        default_time_source: str = None,
        enable_sls_context: bool = None,
        encoding: str = None,
        from_position: str = None,
        name_resolutions: str = None,
        parse_array: bool = None,
        processor_id: str = None,
        time_field: str = None,
        time_format: str = None,
        time_pattern: str = None,
        time_zone: str = None,
        topics: str = None,
        value_type: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.bootstrap_servers = bootstrap_servers
        self.communication = communication
        self.consumer_group = consumer_group
        self.default_time_source = default_time_source
        self.enable_sls_context = enable_sls_context
        # This parameter is required.
        self.encoding = encoding
        # This parameter is required.
        self.from_position = from_position
        self.name_resolutions = name_resolutions
        # This parameter is required.
        self.parse_array = parse_array
        self.processor_id = processor_id
        self.time_field = time_field
        self.time_format = time_format
        self.time_pattern = time_pattern
        self.time_zone = time_zone
        # This parameter is required.
        self.topics = topics
        # This parameter is required.
        self.value_type = value_type
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bootstrap_servers is not None:
            result['bootstrapServers'] = self.bootstrap_servers

        if self.communication is not None:
            result['communication'] = self.communication

        if self.consumer_group is not None:
            result['consumerGroup'] = self.consumer_group

        if self.default_time_source is not None:
            result['defaultTimeSource'] = self.default_time_source

        if self.enable_sls_context is not None:
            result['enableSlsContext'] = self.enable_sls_context

        if self.encoding is not None:
            result['encoding'] = self.encoding

        if self.from_position is not None:
            result['fromPosition'] = self.from_position

        if self.name_resolutions is not None:
            result['nameResolutions'] = self.name_resolutions

        if self.parse_array is not None:
            result['parseArray'] = self.parse_array

        if self.processor_id is not None:
            result['processorId'] = self.processor_id

        if self.time_field is not None:
            result['timeField'] = self.time_field

        if self.time_format is not None:
            result['timeFormat'] = self.time_format

        if self.time_pattern is not None:
            result['timePattern'] = self.time_pattern

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        if self.topics is not None:
            result['topics'] = self.topics

        if self.value_type is not None:
            result['valueType'] = self.value_type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bootstrapServers') is not None:
            self.bootstrap_servers = m.get('bootstrapServers')

        if m.get('communication') is not None:
            self.communication = m.get('communication')

        if m.get('consumerGroup') is not None:
            self.consumer_group = m.get('consumerGroup')

        if m.get('defaultTimeSource') is not None:
            self.default_time_source = m.get('defaultTimeSource')

        if m.get('enableSlsContext') is not None:
            self.enable_sls_context = m.get('enableSlsContext')

        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')

        if m.get('fromPosition') is not None:
            self.from_position = m.get('fromPosition')

        if m.get('nameResolutions') is not None:
            self.name_resolutions = m.get('nameResolutions')

        if m.get('parseArray') is not None:
            self.parse_array = m.get('parseArray')

        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')

        if m.get('timeField') is not None:
            self.time_field = m.get('timeField')

        if m.get('timeFormat') is not None:
            self.time_format = m.get('timeFormat')

        if m.get('timePattern') is not None:
            self.time_pattern = m.get('timePattern')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('topics') is not None:
            self.topics = m.get('topics')

        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

