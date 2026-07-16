# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUnknownThreatDetectMachineRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        remark: str = None,
        status: str = None,
        study_mode: str = None,
        study_time_end: int = None,
        study_time_start: int = None,
        uuid: str = None,
    ):
        # The page number to return.
        self.current_page = current_page
        # The maximum number of entries to return per page.
        self.page_size = page_size
        # The server name or IP address.
        self.remark = remark
        # The status of the machine. Valid values:
        # 
        # - **monitoring**: Monitoring
        # 
        # - **blocking**: Blocking
        # 
        # - **studying**: Learning
        # 
        # - **study_finish**: Learning complete
        self.status = status
        # The whitelist mode. Valid values:
        # 
        # - **hash**: process hash
        # 
        # - **path**: process path
        self.study_mode = study_mode
        # The end of the time range for model creation, specified as a timestamp in milliseconds.
        self.study_time_end = study_time_end
        # The start of the time range for model creation, specified as a timestamp in milliseconds.
        self.study_time_start = study_time_start
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.study_mode is not None:
            result['StudyMode'] = self.study_mode

        if self.study_time_end is not None:
            result['StudyTimeEnd'] = self.study_time_end

        if self.study_time_start is not None:
            result['StudyTimeStart'] = self.study_time_start

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StudyMode') is not None:
            self.study_mode = m.get('StudyMode')

        if m.get('StudyTimeEnd') is not None:
            self.study_time_end = m.get('StudyTimeEnd')

        if m.get('StudyTimeStart') is not None:
            self.study_time_start = m.get('StudyTimeStart')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

