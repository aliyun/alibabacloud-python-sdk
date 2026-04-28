# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class LocationDateCluster(DaraModel):
    def __init__(
        self,
        address: main_models.Address = None,
        cluster_id: str = None,
        created_at: str = None,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        end_time: str = None,
        level: str = None,
        start_time: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        self.address = address
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.custom_labels = custom_labels
        self.drive_id = drive_id
        self.end_time = end_time
        self.level = level
        self.start_time = start_time
        self.title = title
        self.updated_at = updated_at

    def validate(self):
        if self.address:
            self.address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address.to_map()

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.level is not None:
            result['level'] = self.level

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.title is not None:
            result['title'] = self.title

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            temp_model = main_models.Address()
            self.address = temp_model.from_map(m.get('address'))

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

