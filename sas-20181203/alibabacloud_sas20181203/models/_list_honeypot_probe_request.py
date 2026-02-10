# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHoneypotProbeRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        display_name: str = None,
        lang: str = None,
        page_size: int = None,
        probe_status: str = None,
        probe_type: str = None,
    ):
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The name of the probe.
        self.display_name = display_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The status of the probe. Valid values:
        # 
        # *   **installed**: installed
        # *   **install_failed**: installation failed
        # *   **online**: online
        # *   **offline**: offline
        # *   **unnormal**: abnormal
        # *   **unprobe**: unauthorized
        # *   **uninstalling**: being uninstalled
        # *   **uninstalled**: uninstalled
        # *   **uninstall_failed**: uninstallation failed
        # *   **not_exist**: not installed
        self.probe_status = probe_status
        # The type of the probe. Valid values:
        # 
        # *   **host_probe**: host probe
        # *   **vpc_black_hole_probe**: VPC probe
        self.probe_type = probe_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.probe_status is not None:
            result['ProbeStatus'] = self.probe_status

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProbeStatus') is not None:
            self.probe_status = m.get('ProbeStatus')

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        return self

