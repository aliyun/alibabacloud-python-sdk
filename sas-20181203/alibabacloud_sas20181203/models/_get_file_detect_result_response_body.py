# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileDetectResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_list: List[main_models.GetFileDetectResultResponseBodyResultList] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of file detection results.
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.GetFileDetectResultResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k1))

        return self

class GetFileDetectResultResponseBodyResultList(DaraModel):
    def __init__(
        self,
        code: str = None,
        compress: bool = None,
        ext: str = None,
        hash_key: str = None,
        message: str = None,
        result: int = None,
        score: int = None,
        virus_type: str = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # Whether to identify as a compressed package. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.compress = compress
        # The extended information about the file detection result.
        self.ext = ext
        # The identifier of the file. Only MD5 hash values are supported.
        self.hash_key = hash_key
        # The error message returned.
        self.message = message
        # The file detection result. Valid values:
        # 
        # *   **0**: The file is normal.
        # *   **1**: The file is suspicious.
        # *   **3**: The detection is in progress.
        self.result = result
        # The score of file detection result.
        # 
        # > A higher score indicates a more suspicious file.
        self.score = score
        # The type of the virus. Valid values:
        # 
        # *   **Trojan**: trojan horse
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
        if self.code is not None:
            result['Code'] = self.code

        if self.compress is not None:
            result['Compress'] = self.compress

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.message is not None:
            result['Message'] = self.message

        if self.result is not None:
            result['Result'] = self.result

        if self.score is not None:
            result['Score'] = self.score

        if self.virus_type is not None:
            result['VirusType'] = self.virus_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Compress') is not None:
            self.compress = m.get('Compress')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('VirusType') is not None:
            self.virus_type = m.get('VirusType')

        return self

