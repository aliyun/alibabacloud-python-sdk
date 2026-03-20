# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DesignateWorkersRequest(DaraModel):
    def __init__(
        self,
        designate_type: int = None,
        group_id: str = None,
        job_id: int = None,
        labels: str = None,
        namespace: str = None,
        namespace_source: str = None,
        region_id: str = None,
        transferable: bool = None,
        workers: str = None,
    ):
        # The type of the machines to be designated. Valid values: 1 and 2. The value 1 specifies the worker type. The value 2 specifies the label type.
        # 
        # This parameter is required.
        self.designate_type = designate_type
        # The application group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The designated `labels`. Specify the value of the parameter in a `JSON` string.
        self.labels = labels
        # The unique identifier (UID) of the namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace.
        self.namespace_source = namespace_source
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to allow a failover.
        # 
        # This parameter is required.
        self.transferable = transferable
        # The designated machines. Specify the value of the parameter in a JSON string.
        self.workers = workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.transferable is not None:
            result['Transferable'] = self.transferable

        if self.workers is not None:
            result['Workers'] = self.workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')

        if m.get('Workers') is not None:
            self.workers = m.get('Workers')

        return self

