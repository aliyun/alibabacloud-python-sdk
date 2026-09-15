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
        # The identifier of the request source. Set the value to sas.
        self.from_ = from_
        # The ID of the quarantined file.
        # 
        # > If you do not specify this parameter, calling the RollbackSuspEventQuaraFile operation does not cancel the quarantine of the file in the quarantine box, which means the call does not take effect. Call the [DescribeSuspEventQuaraFiles](~~DescribeSuspEventQuaraFiles~~) operation to obtain the quarantined file ID (the value of the Id parameter).
        # 
        # QuaraFileId depends on the following prerequisite chain: (1) The SAS Agent must be installed on the ECS instance and be online. (2) The Agent must detect a malicious file and generate a security alert. (3) The alert must be quarantined by calling the HandleSecurityEvents operation (OperationCode=quara). (4) Call the DescribeSuspEventQuaraFiles operation to obtain the QuaraFileId.
        # 
        # Note: This parameter is actually required. If it is not provided, the API returns error code -101 (400) with the message "The ID of the file to be rolled back is not provided".
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

