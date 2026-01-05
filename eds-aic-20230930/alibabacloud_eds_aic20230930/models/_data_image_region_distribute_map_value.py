# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataImageRegionDistributeMapValue(DaraModel):
    def __init__(
        self,
        distribute_status: str = None,
        progress: str = None,
    ):
        # The status of the image distribution task.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The task is ready.
        # *   DELETE: The task is deleted.
        # *   INIT: The task is being initialized.
        # *   CREATE_FAILED: The task failed to be created.
        # *   CREATING: The task is being created.
        self.distribute_status = distribute_status
        # The distribution progress of the image.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribute_status is not None:
            result['DistributeStatus'] = self.distribute_status

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributeStatus') is not None:
            self.distribute_status = m.get('DistributeStatus')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

