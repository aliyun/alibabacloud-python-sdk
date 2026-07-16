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
        # The timestamp when the binding between the dataset and the OSS bucket was created. The format is RFC3339Nano.
        self.create_time = create_time
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The scan type. Valid values:
        # 
        # - FullScanning: A full scan is in progress.
        # 
        # - IncrementalScanning: An incremental scan is in progress.
        self.phase = phase
        # The name of the project.
        self.project_name = project_name
        # Reason
        self.reason = reason
        # The state of the binding between the dataset and the OSS bucket. Valid values:
        # 
        # - Ready: The binding is being prepared after it is created.
        # 
        # - Stopped: The binding is paused.
        # 
        # - Running: The binding is running.
        # 
        # - Retrying: The binding is being retried after it is created.
        # 
        # - Failed: The binding failed to be created.
        # 
        # - Deleted: The binding is deleted.
        self.state = state
        # The URI of the Object Storage Service (OSS) bucket attached to the dataset.
        # 
        # The format of an OSS bucket URI is `oss://${bucketname}`. The `bucketname` is the name of an OSS bucket that is in the same region as the current project.
        self.uri = uri
        # The timestamp when the binding between the dataset and the OSS bucket was last modified. The format is RFC3339Nano.
        # 
        # > After a binding is created, if the binding has not been paused or restarted, this timestamp is the same as the creation timestamp.
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

