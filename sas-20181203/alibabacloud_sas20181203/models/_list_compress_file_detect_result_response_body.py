# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCompressFileDetectResultResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListCompressFileDetectResultResponseBodyPageInfo = None,
        request_id: str = None,
        result_list: List[main_models.ListCompressFileDetectResultResponseBodyResultList] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The detection results of files.
        self.result_list = result_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCompressFileDetectResultResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.ListCompressFileDetectResultResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k1))

        return self

class ListCompressFileDetectResultResponseBodyResultList(DaraModel):
    def __init__(
        self,
        ext: str = None,
        hash_key: str = None,
        path: str = None,
        result: int = None,
        score: int = None,
        virus_type: str = None,
    ):
        # The extended information about the file detection result.
        self.ext = ext
        # The identifier of the file.
        self.hash_key = hash_key
        # The path to the file within the package.
        self.path = path
        # The file detection result. Valid values:
        # 
        # *   **0**: The file is normal.
        # *   **1**: The file is suspicious.
        # *   **3**: The detection is in progress.
        self.result = result
        # The score of the file detection result. The following list describes mappings between the score ranges and risk levels:
        # 
        # *   0 to 60: normal
        # *   61 to 70: risky
        # *   71 to 80: suspicious
        # *   81 to 100: malicious
        # 
        # >  A higher score indicates a more suspicious file.
        self.score = score
        # The type of the virus. Valid values:
        # 
        # *   **Trojan**: self-mutating trojan
        # *   **WebShell**: webshell
        # *   **Backdoor**: backdoor program
        # *   **RansomWare**: ransomware
        # *   **Scanner**: scanner
        # *   **Stealer**: tool that is used to steal information
        # *   **Malbaseware**: tainted basic software
        # *   **Hacktool**: attacker tool
        # *   **Engtest**: engine test program
        # *   **Downloader**: trojan downloader
        # *   **Virus**: infectious virus
        # *   **Miner**: mining program
        # *   **Worm**: worm
        # *   **DDoS**: DDoS trojan
        # *   **Malware**: malicious program
        # *   **Backdoor**: reverse shell
        # *   **RiskWare**: software that has risks
        # *   **Proxytool**: proxy
        # *   **Suspicious**: suspicious program
        # *   **MalScript**: malicious script
        # *   **Rootkit**: rootkit
        # *   **Exploit**: exploit
        self.virus_type = virus_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.path is not None:
            result['Path'] = self.path

        if self.result is not None:
            result['Result'] = self.result

        if self.score is not None:
            result['Score'] = self.score

        if self.virus_type is not None:
            result['VirusType'] = self.virus_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('VirusType') is not None:
            self.virus_type = m.get('VirusType')

        return self

class ListCompressFileDetectResultResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

