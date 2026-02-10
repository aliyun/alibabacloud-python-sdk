# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspEventQuaraFilesRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        from_: str = None,
        group_id: str = None,
        grouping_id: int = None,
        page_size: str = None,
        quara_tag: str = None,
        source_ip: str = None,
        status: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The ID of the request source. Set the value to **sas**.
        self.from_ = from_
        # The ID of the asset group.
        self.group_id = group_id
        # The ID of the server group to which the server belongs. The quarantined file is located on the server.
        self.grouping_id = grouping_id
        # The number of entries to return on each page.
        self.page_size = page_size
        # The unique ID of the quarantined file.
        self.quara_tag = quara_tag
        # The source IP address of the request.
        self.source_ip = source_ip
        # The status of the quarantined file that you want to query. Valid values:
        # 
        # *   **quaraFailed**: The file fails to be quarantined.
        # *   **quaraDone**: The file is quarantined.
        # *   **quaraing**: The file is being quarantined.
        # *   **rollbackFailed**: The system fails to cancel quarantining the file.
        # *   **rollbackDone**: The system cancelled quarantining the file.
        # *   **rollbacking**: The system is cancelling quarantining the file.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.from_ is not None:
            result['From'] = self.from_

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.grouping_id is not None:
            result['GroupingId'] = self.grouping_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.quara_tag is not None:
            result['QuaraTag'] = self.quara_tag

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupingId') is not None:
            self.grouping_id = m.get('GroupingId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QuaraTag') is not None:
            self.quara_tag = m.get('QuaraTag')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

