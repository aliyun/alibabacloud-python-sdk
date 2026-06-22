# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQuaraFileDownloadInfoRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        quara_file_id: int = None,
    ):
        # The source identifier of the request. Set the value to sas.
        self.from_ = from_
        # The ID of the quarantined file.
        # 
        # > If you do not specify this parameter, calling the RollbackSuspEventQuaraFile operation does not cancel the quarantine of the file in the quarantine box, which means the call does not take effect. Call the [DescribeSuspEventQuaraFiles](~~DescribeSuspEventQuaraFiles~~) operation to obtain the quarantined file ID (the value of the Id parameter).
        self.quara_file_id = quara_file_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('QuaraFileId') is not None:
            self.quara_file_id = m.get('QuaraFileId')

        return self

