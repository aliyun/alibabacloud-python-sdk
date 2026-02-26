# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLocationDateClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        title: str = None,
    ):
        # The custom ID of the cluster. When the cluster is indexed into the dataset, the custom ID is stored as the data attribute. You can map the custom ID to other data in your business system. For example, you can pass the custom ID to map a URI to an ID. We recommend that you specify a globally unique value. The value can be up to 1,024 bytes in size.
        self.custom_id = custom_id
        # The custom labels. The parameter stores custom key-value labels, which can be used to filter data. You can specify up to 100 custom labels for a cluster.
        self.custom_labels_shrink = custom_labels_shrink
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The ID of the cluster that you want to update.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the cluster. The name can be used to search for the cluster. The value can be up to 1,024 bytes in size.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

