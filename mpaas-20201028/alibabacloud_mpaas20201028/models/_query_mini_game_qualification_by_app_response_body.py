# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMiniGameQualificationByAppResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        content: List[main_models.QueryMiniGameQualificationByAppResponseBodyContent] = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.QueryMiniGameQualificationByAppResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMiniGameQualificationByAppResponseBodyContent(DaraModel):
    def __init__(
        self,
        business_license_name: str = None,
        business_license_url: str = None,
        copyright_authorization_files: List[main_models.QueryMiniGameQualificationByAppResponseBodyContentCopyrightAuthorizationFiles] = None,
        copyright_file_name: str = None,
        copyright_registration_number: str = None,
        copyright_url: str = None,
        developer: str = None,
        game_type: str = None,
        game_version_id: str = None,
        gmt_modified: int = None,
        icp_file_name: str = None,
        icp_url: str = None,
        id_code: str = None,
        ip_authorization_files: List[main_models.QueryMiniGameQualificationByAppResponseBodyContentIpAuthorizationFiles] = None,
        mini_program_code: str = None,
        mini_program_id: int = None,
        online_game_pub_re_file_name: str = None,
        online_game_pub_re_url: str = None,
        privacy_policy_url: str = None,
        publisher: str = None,
        review_status: str = None,
    ):
        self.business_license_name = business_license_name
        self.business_license_url = business_license_url
        self.copyright_authorization_files = copyright_authorization_files
        self.copyright_file_name = copyright_file_name
        self.copyright_registration_number = copyright_registration_number
        self.copyright_url = copyright_url
        self.developer = developer
        self.game_type = game_type
        self.game_version_id = game_version_id
        self.gmt_modified = gmt_modified
        self.icp_file_name = icp_file_name
        self.icp_url = icp_url
        self.id_code = id_code
        self.ip_authorization_files = ip_authorization_files
        self.mini_program_code = mini_program_code
        self.mini_program_id = mini_program_id
        self.online_game_pub_re_file_name = online_game_pub_re_file_name
        self.online_game_pub_re_url = online_game_pub_re_url
        self.privacy_policy_url = privacy_policy_url
        self.publisher = publisher
        self.review_status = review_status

    def validate(self):
        if self.copyright_authorization_files:
            for v1 in self.copyright_authorization_files:
                 if v1:
                    v1.validate()
        if self.ip_authorization_files:
            for v1 in self.ip_authorization_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_license_name is not None:
            result['BusinessLicenseName'] = self.business_license_name

        if self.business_license_url is not None:
            result['BusinessLicenseUrl'] = self.business_license_url

        result['CopyrightAuthorizationFiles'] = []
        if self.copyright_authorization_files is not None:
            for k1 in self.copyright_authorization_files:
                result['CopyrightAuthorizationFiles'].append(k1.to_map() if k1 else None)

        if self.copyright_file_name is not None:
            result['CopyrightFileName'] = self.copyright_file_name

        if self.copyright_registration_number is not None:
            result['CopyrightRegistrationNumber'] = self.copyright_registration_number

        if self.copyright_url is not None:
            result['CopyrightUrl'] = self.copyright_url

        if self.developer is not None:
            result['Developer'] = self.developer

        if self.game_type is not None:
            result['GameType'] = self.game_type

        if self.game_version_id is not None:
            result['GameVersionId'] = self.game_version_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icp_file_name is not None:
            result['IcpFileName'] = self.icp_file_name

        if self.icp_url is not None:
            result['IcpUrl'] = self.icp_url

        if self.id_code is not None:
            result['IdCode'] = self.id_code

        result['IpAuthorizationFiles'] = []
        if self.ip_authorization_files is not None:
            for k1 in self.ip_authorization_files:
                result['IpAuthorizationFiles'].append(k1.to_map() if k1 else None)

        if self.mini_program_code is not None:
            result['MiniProgramCode'] = self.mini_program_code

        if self.mini_program_id is not None:
            result['MiniProgramId'] = self.mini_program_id

        if self.online_game_pub_re_file_name is not None:
            result['OnlineGamePubReFileName'] = self.online_game_pub_re_file_name

        if self.online_game_pub_re_url is not None:
            result['OnlineGamePubReUrl'] = self.online_game_pub_re_url

        if self.privacy_policy_url is not None:
            result['PrivacyPolicyUrl'] = self.privacy_policy_url

        if self.publisher is not None:
            result['Publisher'] = self.publisher

        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessLicenseName') is not None:
            self.business_license_name = m.get('BusinessLicenseName')

        if m.get('BusinessLicenseUrl') is not None:
            self.business_license_url = m.get('BusinessLicenseUrl')

        self.copyright_authorization_files = []
        if m.get('CopyrightAuthorizationFiles') is not None:
            for k1 in m.get('CopyrightAuthorizationFiles'):
                temp_model = main_models.QueryMiniGameQualificationByAppResponseBodyContentCopyrightAuthorizationFiles()
                self.copyright_authorization_files.append(temp_model.from_map(k1))

        if m.get('CopyrightFileName') is not None:
            self.copyright_file_name = m.get('CopyrightFileName')

        if m.get('CopyrightRegistrationNumber') is not None:
            self.copyright_registration_number = m.get('CopyrightRegistrationNumber')

        if m.get('CopyrightUrl') is not None:
            self.copyright_url = m.get('CopyrightUrl')

        if m.get('Developer') is not None:
            self.developer = m.get('Developer')

        if m.get('GameType') is not None:
            self.game_type = m.get('GameType')

        if m.get('GameVersionId') is not None:
            self.game_version_id = m.get('GameVersionId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IcpFileName') is not None:
            self.icp_file_name = m.get('IcpFileName')

        if m.get('IcpUrl') is not None:
            self.icp_url = m.get('IcpUrl')

        if m.get('IdCode') is not None:
            self.id_code = m.get('IdCode')

        self.ip_authorization_files = []
        if m.get('IpAuthorizationFiles') is not None:
            for k1 in m.get('IpAuthorizationFiles'):
                temp_model = main_models.QueryMiniGameQualificationByAppResponseBodyContentIpAuthorizationFiles()
                self.ip_authorization_files.append(temp_model.from_map(k1))

        if m.get('MiniProgramCode') is not None:
            self.mini_program_code = m.get('MiniProgramCode')

        if m.get('MiniProgramId') is not None:
            self.mini_program_id = m.get('MiniProgramId')

        if m.get('OnlineGamePubReFileName') is not None:
            self.online_game_pub_re_file_name = m.get('OnlineGamePubReFileName')

        if m.get('OnlineGamePubReUrl') is not None:
            self.online_game_pub_re_url = m.get('OnlineGamePubReUrl')

        if m.get('PrivacyPolicyUrl') is not None:
            self.privacy_policy_url = m.get('PrivacyPolicyUrl')

        if m.get('Publisher') is not None:
            self.publisher = m.get('Publisher')

        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')

        return self

class QueryMiniGameQualificationByAppResponseBodyContentIpAuthorizationFiles(DaraModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class QueryMiniGameQualificationByAppResponseBodyContentCopyrightAuthorizationFiles(DaraModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

