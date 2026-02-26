# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class LocationDateCluster(DaraModel):
    def __init__(
        self,
        addresses: List[main_models.Address] = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        location_date_cluster_end_time: str = None,
        location_date_cluster_level: str = None,
        location_date_cluster_start_time: str = None,
        object_id: str = None,
        title: str = None,
        update_time: str = None,
    ):
        # The addresses.
        self.addresses = addresses
        # The time when the spatiotemporal cluster was created.
        self.create_time = create_time
        # The custom ID.
        self.custom_id = custom_id
        # The custom labels.
        self.custom_labels = custom_labels
        # The end time of the spatiotemporal cluster.
        self.location_date_cluster_end_time = location_date_cluster_end_time
        # The administrative level of the spatiotemporal cluster.
        # 
        # Enumerated values:
        # 
        # *   country
        # *   province
        # *   city
        # *   district
        # *   township
        self.location_date_cluster_level = location_date_cluster_level
        # The start time of the spatiotemporal cluster.
        self.location_date_cluster_start_time = location_date_cluster_start_time
        # The cluster ID.
        self.object_id = object_id
        # The custom title.
        self.title = title
        # The time when the spatiotemporal cluster was updated.
        self.update_time = update_time

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.location_date_cluster_end_time is not None:
            result['LocationDateClusterEndTime'] = self.location_date_cluster_end_time

        if self.location_date_cluster_level is not None:
            result['LocationDateClusterLevel'] = self.location_date_cluster_level

        if self.location_date_cluster_start_time is not None:
            result['LocationDateClusterStartTime'] = self.location_date_cluster_start_time

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.Address()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('LocationDateClusterEndTime') is not None:
            self.location_date_cluster_end_time = m.get('LocationDateClusterEndTime')

        if m.get('LocationDateClusterLevel') is not None:
            self.location_date_cluster_level = m.get('LocationDateClusterLevel')

        if m.get('LocationDateClusterStartTime') is not None:
            self.location_date_cluster_start_time = m.get('LocationDateClusterStartTime')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

