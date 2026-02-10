# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackSuspEventQuaraFileRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        quara_file_id: int = None,
        source_ip: str = None,
    ):
        # The ID of the request source. Set the value to sas.
        self.from_ = from_
        # The ID of the quarantined file.   
        # > If you do not configure this parameter, you cannot call the RollbackSuspEventQuaraFile operation to restore a quarantined file. You can call the [DescribeSuspEventQuaraFiles](~~DescribeSuspEventQuaraFiles~~) operation to query the IDs of quarantined files.
        self.quara_file_id = quara_file_id
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.quara_file_id is not None:
            result['QuaraFileId'] = self.quara_file_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('QuaraFileId') is not None:
            self.quara_file_id = m.get('QuaraFileId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

