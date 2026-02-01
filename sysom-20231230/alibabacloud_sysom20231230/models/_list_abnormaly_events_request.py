# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAbnormalyEventsRequest(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        current: int = None,
        end: float = None,
        event: str = None,
        instance: str = None,
        level: str = None,
        namespace: str = None,
        page_size: int = None,
        pod: str = None,
        show_pod: int = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.current = current
        self.end = end
        self.event = event
        self.instance = instance
        self.level = level
        self.namespace = namespace
        self.page_size = page_size
        self.pod = pod
        self.show_pod = show_pod
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.current is not None:
            result['current'] = self.current

        if self.end is not None:
            result['end'] = self.end

        if self.event is not None:
            result['event'] = self.event

        if self.instance is not None:
            result['instance'] = self.instance

        if self.level is not None:
            result['level'] = self.level

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.pod is not None:
            result['pod'] = self.pod

        if self.show_pod is not None:
            result['showPod'] = self.show_pod

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pod') is not None:
            self.pod = m.get('pod')

        if m.get('showPod') is not None:
            self.show_pod = m.get('showPod')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

