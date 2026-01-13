# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSampleConsistencyJobRequest(DaraModel):
    def __init__(
        self,
        duration: str = None,
        eas_model_service_name: str = None,
        feature_save_resource_id: str = None,
        instance_id: str = None,
        item_id_field: str = None,
        name: str = None,
        partition_field: str = None,
        partition_field_format: str = None,
        request_id_field: str = None,
        sample_rate: str = None,
        sample_table_name: str = None,
        scene_id: str = None,
        user_id_field: str = None,
    ):
        self.duration = duration
        self.eas_model_service_name = eas_model_service_name
        self.feature_save_resource_id = feature_save_resource_id
        # This parameter is required.
        self.instance_id = instance_id
        self.item_id_field = item_id_field
        self.name = name
        self.partition_field = partition_field
        self.partition_field_format = partition_field_format
        self.request_id_field = request_id_field
        self.sample_rate = sample_rate
        self.sample_table_name = sample_table_name
        self.scene_id = scene_id
        self.user_id_field = user_id_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.eas_model_service_name is not None:
            result['EasModelServiceName'] = self.eas_model_service_name

        if self.feature_save_resource_id is not None:
            result['FeatureSaveResourceId'] = self.feature_save_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_id_field is not None:
            result['ItemIdField'] = self.item_id_field

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_field is not None:
            result['PartitionField'] = self.partition_field

        if self.partition_field_format is not None:
            result['PartitionFieldFormat'] = self.partition_field_format

        if self.request_id_field is not None:
            result['RequestIdField'] = self.request_id_field

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.sample_table_name is not None:
            result['SampleTableName'] = self.sample_table_name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.user_id_field is not None:
            result['UserIdField'] = self.user_id_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EasModelServiceName') is not None:
            self.eas_model_service_name = m.get('EasModelServiceName')

        if m.get('FeatureSaveResourceId') is not None:
            self.feature_save_resource_id = m.get('FeatureSaveResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemIdField') is not None:
            self.item_id_field = m.get('ItemIdField')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionField') is not None:
            self.partition_field = m.get('PartitionField')

        if m.get('PartitionFieldFormat') is not None:
            self.partition_field_format = m.get('PartitionFieldFormat')

        if m.get('RequestIdField') is not None:
            self.request_id_field = m.get('RequestIdField')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('SampleTableName') is not None:
            self.sample_table_name = m.get('SampleTableName')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('UserIdField') is not None:
            self.user_id_field = m.get('UserIdField')

        return self

