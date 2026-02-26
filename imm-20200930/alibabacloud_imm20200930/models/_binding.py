# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Binding(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_name: str = None,
        phase: str = None,
        project_name: str = None,
        reason: str = None,
        state: str = None,
        uri: str = None,
        update_time: str = None,
    ):
        # The RFC3339Nano timestamp when the OSS bucket was bound to the dataset.
        self.create_time = create_time
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The type of the scan. Valid values:
        # 
        # *   FullScanning
        # *   IncrementalScanning
        self.phase = phase
        # The name of the project.
        self.project_name = project_name
        # Reason
        self.reason = reason
        # The status of the binding between the dataset and the OSS bucket. Valid values:
        # 
        # *   Ready: IMM is ready to create the binding.
        # *   Stopped: The binding creation is suspended.
        # *   Running: The binding is running.
        # *   Retrying: IMM is retrying the binding.
        # *   Failed: The binding failed.
        # *   Deleted: The binding is deleted.
        self.state = state
        # The URI of the OSS bucket to which the dataset is bound.
        # 
        # The URI is in the `oss://${bucketname}` format, where `bucketname` is the name of the OSS bucket.
        self.uri = uri
        # The RFC3339Nano timestamp when the binding was modified.
        # 
        # >  If you never suspend or retry the binding between the dataset and the OSS bucket after you complete the binding, the value of UpdateTime is the same as that of CreateTime.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.state is not None:
            result['State'] = self.state

        if self.uri is not None:
            result['URI'] = self.uri

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

