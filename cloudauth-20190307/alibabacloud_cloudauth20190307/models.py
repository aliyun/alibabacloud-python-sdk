# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, BinaryIO
except ImportError:
    pass


class DescribeFaceConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['Lang'] = self.lang
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.lang = map.get('Lang')
        return self


class DescribeFaceConfigResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id    # type: str
        self.items = items              # type: List[DescribeFaceConfigResponseItems]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.items = []
        if map.get('Items') is not None:
            for k in map.get('Items'):
                temp_model = DescribeFaceConfigResponseItems()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        return self


class DescribeFaceConfigResponseItems(TeaModel):
    def __init__(self, biz_type=None, biz_name=None, gmt_updated=None):
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str
        self.gmt_updated = gmt_updated  # type: int

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.gmt_updated, 'gmt_updated')

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        result['GmtUpdated'] = self.gmt_updated
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        self.gmt_updated = map.get('GmtUpdated')
        return self


class UpdateFaceConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, biz_type=None, biz_name=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['Lang'] = self.lang
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.lang = map.get('Lang')
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        return self


class UpdateFaceConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateFaceConfigRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, biz_type=None, biz_name=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['Lang'] = self.lang
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.lang = map.get('Lang')
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        return self


class CreateFaceConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class LivenessFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, face_contrast_picture=None,
                 device_token=None, mobile=None, ip=None, user_id=None, face_contrast_picture_url=None, certify_id=None,
                 oss_bucket_name=None, oss_object_name=None, model=None):
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.device_token = device_token  # type: str
        self.mobile = mobile            # type: str
        self.ip = ip                    # type: str
        self.user_id = user_id          # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id    # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['ProductCode'] = self.product_code
        result['FaceContrastPicture'] = self.face_contrast_picture
        result['DeviceToken'] = self.device_token
        result['Mobile'] = self.mobile
        result['Ip'] = self.ip
        result['UserId'] = self.user_id
        result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        result['CertifyId'] = self.certify_id
        result['OssBucketName'] = self.oss_bucket_name
        result['OssObjectName'] = self.oss_object_name
        result['Model'] = self.model
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.product_code = map.get('ProductCode')
        self.face_contrast_picture = map.get('FaceContrastPicture')
        self.device_token = map.get('DeviceToken')
        self.mobile = map.get('Mobile')
        self.ip = map.get('Ip')
        self.user_id = map.get('UserId')
        self.face_contrast_picture_url = map.get('FaceContrastPictureUrl')
        self.certify_id = map.get('CertifyId')
        self.oss_bucket_name = map.get('OssBucketName')
        self.oss_object_name = map.get('OssObjectName')
        self.model = map.get('Model')
        return self


class LivenessFaceVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: LivenessFaceVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = LivenessFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class LivenessFaceVerifyResponseResultObject(TeaModel):
    def __init__(self, passed=None, material_info=None, sub_code=None):
        self.passed = passed            # type: str
        self.material_info = material_info  # type: str
        self.sub_code = sub_code        # type: str

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.sub_code, 'sub_code')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['MaterialInfo'] = self.material_info
        result['SubCode'] = self.sub_code
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.material_info = map.get('MaterialInfo')
        self.sub_code = map.get('SubCode')
        return self


class CompareFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, source_face_contrast_picture=None,
                 source_face_contrast_picture_url=None, source_certify_id=None, source_oss_bucket_name=None, source_oss_object_name=None,
                 target_face_contrast_picture=None, target_face_contrast_picture_url=None, target_certify_id=None, target_oss_bucket_name=None,
                 target_oss_object_name=None):
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.source_face_contrast_picture = source_face_contrast_picture  # type: str
        self.source_face_contrast_picture_url = source_face_contrast_picture_url  # type: str
        self.source_certify_id = source_certify_id  # type: str
        self.source_oss_bucket_name = source_oss_bucket_name  # type: str
        self.source_oss_object_name = source_oss_object_name  # type: str
        self.target_face_contrast_picture = target_face_contrast_picture  # type: str
        self.target_face_contrast_picture_url = target_face_contrast_picture_url  # type: str
        self.target_certify_id = target_certify_id  # type: str
        self.target_oss_bucket_name = target_oss_bucket_name  # type: str
        self.target_oss_object_name = target_oss_object_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['ProductCode'] = self.product_code
        result['SourceFaceContrastPicture'] = self.source_face_contrast_picture
        result['SourceFaceContrastPictureUrl'] = self.source_face_contrast_picture_url
        result['SourceCertifyId'] = self.source_certify_id
        result['SourceOssBucketName'] = self.source_oss_bucket_name
        result['SourceOssObjectName'] = self.source_oss_object_name
        result['TargetFaceContrastPicture'] = self.target_face_contrast_picture
        result['TargetFaceContrastPictureUrl'] = self.target_face_contrast_picture_url
        result['TargetCertifyId'] = self.target_certify_id
        result['TargetOssBucketName'] = self.target_oss_bucket_name
        result['TargetOssObjectName'] = self.target_oss_object_name
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.product_code = map.get('ProductCode')
        self.source_face_contrast_picture = map.get('SourceFaceContrastPicture')
        self.source_face_contrast_picture_url = map.get('SourceFaceContrastPictureUrl')
        self.source_certify_id = map.get('SourceCertifyId')
        self.source_oss_bucket_name = map.get('SourceOssBucketName')
        self.source_oss_object_name = map.get('SourceOssObjectName')
        self.target_face_contrast_picture = map.get('TargetFaceContrastPicture')
        self.target_face_contrast_picture_url = map.get('TargetFaceContrastPictureUrl')
        self.target_certify_id = map.get('TargetCertifyId')
        self.target_oss_bucket_name = map.get('TargetOssBucketName')
        self.target_oss_object_name = map.get('TargetOssObjectName')
        return self


class CompareFaceVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: CompareFaceVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = CompareFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class CompareFaceVerifyResponseResultObject(TeaModel):
    def __init__(self, passed=None, verify_score=None):
        self.passed = passed            # type: str
        self.verify_score = verify_score  # type: float

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.verify_score, 'verify_score')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['VerifyScore'] = self.verify_score
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.verify_score = map.get('VerifyScore')
        return self


class DescribeSdkUrlRequest(TeaModel):
    def __init__(self, id=None, debug=None):
        self.id = id                    # type: int
        self.debug = debug              # type: bool

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Debug'] = self.debug
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.debug = map.get('Debug')
        return self


class DescribeSdkUrlResponse(TeaModel):
    def __init__(self, request_id=None, sdk_url=None):
        self.request_id = request_id    # type: str
        self.sdk_url = sdk_url          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sdk_url, 'sdk_url')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.sdk_url = map.get('SdkUrl')
        return self


class DescribeUpdatePackageResultRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        return self


class DescribeUpdatePackageResultResponse(TeaModel):
    def __init__(self, request_id=None, app_info=None):
        self.request_id = request_id    # type: str
        self.app_info = app_info        # type: DescribeUpdatePackageResultResponseAppInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_info, 'app_info')
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        else:
            result['AppInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('AppInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseAppInfo()
            self.app_info = temp_model.from_map(map['AppInfo'])
        else:
            self.app_info = None
        return self


class DescribeUpdatePackageResultResponseAppInfoPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeUpdatePackageResultResponseAppInfoDebugPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeUpdatePackageResultResponseAppInfo(TeaModel):
    def __init__(self, id=None, name=None, package_name=None, icon=None, start_date=None, end_date=None, type=None,
                 package_info=None, debug_package_info=None):
        self.id = id                    # type: int
        self.name = name                # type: str
        self.package_name = package_name  # type: str
        self.icon = icon                # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.type = type                # type: int
        self.package_info = package_info  # type: DescribeUpdatePackageResultResponseAppInfoPackageInfo
        self.debug_package_info = debug_package_info  # type: DescribeUpdatePackageResultResponseAppInfoDebugPackageInfo

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.package_name, 'package_name')
        self.validate_required(self.icon, 'icon')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.type, 'type')
        self.validate_required(self.package_info, 'package_info')
        if self.package_info:
            self.package_info.validate()
        self.validate_required(self.debug_package_info, 'debug_package_info')
        if self.debug_package_info:
            self.debug_package_info.validate()

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Name'] = self.name
        result['PackageName'] = self.package_name
        result['Icon'] = self.icon
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['Type'] = self.type
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        else:
            result['PackageInfo'] = None
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        else:
            result['DebugPackageInfo'] = None
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.name = map.get('Name')
        self.package_name = map.get('PackageName')
        self.icon = map.get('Icon')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.type = map.get('Type')
        if map.get('PackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseAppInfoPackageInfo()
            self.package_info = temp_model.from_map(map['PackageInfo'])
        else:
            self.package_info = None
        if map.get('DebugPackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseAppInfoDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(map['DebugPackageInfo'])
        else:
            self.debug_package_info = None
        return self


class UpdateAppPackageRequest(TeaModel):
    def __init__(self, id=None, package_url=None, platform=None, debug=None):
        self.id = id                    # type: int
        self.package_url = package_url  # type: str
        self.platform = platform        # type: str
        self.debug = debug              # type: bool

    def validate(self):
        self.validate_required(self.package_url, 'package_url')

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['PackageUrl'] = self.package_url
        result['Platform'] = self.platform
        result['Debug'] = self.debug
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.package_url = map.get('PackageUrl')
        self.platform = map.get('Platform')
        self.debug = map.get('Debug')
        return self


class UpdateAppPackageResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class DescribeAppInfoRequest(TeaModel):
    def __init__(self, page_size=None, current_page=None, platform=None):
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.platform = platform        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['Platform'] = self.platform
        return result

    def from_map(self, map={}):
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.platform = map.get('Platform')
        return self


class DescribeAppInfoResponse(TeaModel):
    def __init__(self, request_id=None, page_size=None, current_page=None, total_count=None, app_info_list=None):
        self.request_id = request_id    # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.total_count = total_count  # type: int
        self.app_info_list = app_info_list  # type: List[DescribeAppInfoResponseAppInfoList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.app_info_list, 'app_info_list')
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['TotalCount'] = self.total_count
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        else:
            result['AppInfoList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.total_count = map.get('TotalCount')
        self.app_info_list = []
        if map.get('AppInfoList') is not None:
            for k in map.get('AppInfoList'):
                temp_model = DescribeAppInfoResponseAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        else:
            self.app_info_list = None
        return self


class DescribeAppInfoResponseAppInfoListPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeAppInfoResponseAppInfoListDebugPackageInfo(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeAppInfoResponseAppInfoList(TeaModel):
    def __init__(self, id=None, name=None, package_name=None, icon=None, start_date=None, end_date=None, type=None,
                 package_info=None, debug_package_info=None):
        self.id = id                    # type: int
        self.name = name                # type: str
        self.package_name = package_name  # type: str
        self.icon = icon                # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.type = type                # type: int
        self.package_info = package_info  # type: DescribeAppInfoResponseAppInfoListPackageInfo
        self.debug_package_info = debug_package_info  # type: DescribeAppInfoResponseAppInfoListDebugPackageInfo

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.package_name, 'package_name')
        self.validate_required(self.icon, 'icon')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.type, 'type')
        self.validate_required(self.package_info, 'package_info')
        if self.package_info:
            self.package_info.validate()
        self.validate_required(self.debug_package_info, 'debug_package_info')
        if self.debug_package_info:
            self.debug_package_info.validate()

    def to_map(self):
        result = {}
        result['Id'] = self.id
        result['Name'] = self.name
        result['PackageName'] = self.package_name
        result['Icon'] = self.icon
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['Type'] = self.type
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        else:
            result['PackageInfo'] = None
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        else:
            result['DebugPackageInfo'] = None
        return result

    def from_map(self, map={}):
        self.id = map.get('Id')
        self.name = map.get('Name')
        self.package_name = map.get('PackageName')
        self.icon = map.get('Icon')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.type = map.get('Type')
        if map.get('PackageInfo') is not None:
            temp_model = DescribeAppInfoResponseAppInfoListPackageInfo()
            self.package_info = temp_model.from_map(map['PackageInfo'])
        else:
            self.package_info = None
        if map.get('DebugPackageInfo') is not None:
            temp_model = DescribeAppInfoResponseAppInfoListDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(map['DebugPackageInfo'])
        else:
            self.debug_package_info = None
        return self


class ContrastFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, cert_type=None, cert_name=None,
                 cert_no=None, face_contrast_picture=None, device_token=None, mobile=None, ip=None, user_id=None,
                 face_contrast_picture_url=None, certify_id=None, oss_bucket_name=None, oss_object_name=None, model=None,
                 face_contrast_file=None):
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.cert_type = cert_type      # type: str
        self.cert_name = cert_name      # type: str
        self.cert_no = cert_no          # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.device_token = device_token  # type: str
        self.mobile = mobile            # type: str
        self.ip = ip                    # type: str
        self.user_id = user_id          # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id    # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model              # type: str
        self.face_contrast_file = face_contrast_file  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['ProductCode'] = self.product_code
        result['CertType'] = self.cert_type
        result['CertName'] = self.cert_name
        result['CertNo'] = self.cert_no
        result['FaceContrastPicture'] = self.face_contrast_picture
        result['DeviceToken'] = self.device_token
        result['Mobile'] = self.mobile
        result['Ip'] = self.ip
        result['UserId'] = self.user_id
        result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        result['CertifyId'] = self.certify_id
        result['OssBucketName'] = self.oss_bucket_name
        result['OssObjectName'] = self.oss_object_name
        result['Model'] = self.model
        result['FaceContrastFile'] = self.face_contrast_file
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.product_code = map.get('ProductCode')
        self.cert_type = map.get('CertType')
        self.cert_name = map.get('CertName')
        self.cert_no = map.get('CertNo')
        self.face_contrast_picture = map.get('FaceContrastPicture')
        self.device_token = map.get('DeviceToken')
        self.mobile = map.get('Mobile')
        self.ip = map.get('Ip')
        self.user_id = map.get('UserId')
        self.face_contrast_picture_url = map.get('FaceContrastPictureUrl')
        self.certify_id = map.get('CertifyId')
        self.oss_bucket_name = map.get('OssBucketName')
        self.oss_object_name = map.get('OssObjectName')
        self.model = map.get('Model')
        self.face_contrast_file = map.get('FaceContrastFile')
        return self


class ContrastFaceVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: ContrastFaceVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = ContrastFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class ContrastFaceVerifyResponseResultObject(TeaModel):
    def __init__(self, passed=None, identity_info=None, material_info=None, sub_code=None):
        self.passed = passed            # type: str
        self.identity_info = identity_info  # type: str
        self.material_info = material_info  # type: str
        self.sub_code = sub_code        # type: str

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.identity_info, 'identity_info')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.sub_code, 'sub_code')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['IdentityInfo'] = self.identity_info
        result['MaterialInfo'] = self.material_info
        result['SubCode'] = self.sub_code
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.identity_info = map.get('IdentityInfo')
        self.material_info = map.get('MaterialInfo')
        self.sub_code = map.get('SubCode')
        return self


class ContrastFaceVerifyAdvanceRequest(TeaModel):
    def __init__(self, face_contrast_file_object=None, scene_id=None, outer_order_no=None, product_code=None,
                 cert_type=None, cert_name=None, cert_no=None, face_contrast_picture=None, device_token=None, mobile=None,
                 ip=None, user_id=None, face_contrast_picture_url=None, certify_id=None, oss_bucket_name=None,
                 oss_object_name=None, model=None):
        self.face_contrast_file_object = face_contrast_file_object  # type: BinaryIO
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.cert_type = cert_type      # type: str
        self.cert_name = cert_name      # type: str
        self.cert_no = cert_no          # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.device_token = device_token  # type: str
        self.mobile = mobile            # type: str
        self.ip = ip                    # type: str
        self.user_id = user_id          # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id    # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model              # type: str

    def validate(self):
        self.validate_required(self.face_contrast_file_object, 'face_contrast_file_object')

    def to_map(self):
        result = {}
        result['FaceContrastFileObject'] = self.face_contrast_file_object
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['ProductCode'] = self.product_code
        result['CertType'] = self.cert_type
        result['CertName'] = self.cert_name
        result['CertNo'] = self.cert_no
        result['FaceContrastPicture'] = self.face_contrast_picture
        result['DeviceToken'] = self.device_token
        result['Mobile'] = self.mobile
        result['Ip'] = self.ip
        result['UserId'] = self.user_id
        result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        result['CertifyId'] = self.certify_id
        result['OssBucketName'] = self.oss_bucket_name
        result['OssObjectName'] = self.oss_object_name
        result['Model'] = self.model
        return result

    def from_map(self, map={}):
        self.face_contrast_file_object = map.get('FaceContrastFileObject')
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.product_code = map.get('ProductCode')
        self.cert_type = map.get('CertType')
        self.cert_name = map.get('CertName')
        self.cert_no = map.get('CertNo')
        self.face_contrast_picture = map.get('FaceContrastPicture')
        self.device_token = map.get('DeviceToken')
        self.mobile = map.get('Mobile')
        self.ip = map.get('Ip')
        self.user_id = map.get('UserId')
        self.face_contrast_picture_url = map.get('FaceContrastPictureUrl')
        self.certify_id = map.get('CertifyId')
        self.oss_bucket_name = map.get('OssBucketName')
        self.oss_object_name = map.get('OssObjectName')
        self.model = map.get('Model')
        return self


class InitDeviceRequest(TeaModel):
    def __init__(self, certify_id=None, outer_order_no=None, channel=None, merchant=None, product_name=None,
                 produce_node=None, biz_data=None, meta_info=None, certify_principal=None, app_version=None, device_token=None,
                 ua_token=None, web_umid_token=None):
        self.certify_id = certify_id    # type: str
        self.outer_order_no = outer_order_no  # type: str
        self.channel = channel          # type: str
        self.merchant = merchant        # type: str
        self.product_name = product_name  # type: str
        self.produce_node = produce_node  # type: str
        self.biz_data = biz_data        # type: str
        self.meta_info = meta_info      # type: str
        self.certify_principal = certify_principal  # type: str
        self.app_version = app_version  # type: str
        self.device_token = device_token  # type: str
        self.ua_token = ua_token        # type: str
        self.web_umid_token = web_umid_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CertifyId'] = self.certify_id
        result['OuterOrderNo'] = self.outer_order_no
        result['Channel'] = self.channel
        result['Merchant'] = self.merchant
        result['ProductName'] = self.product_name
        result['ProduceNode'] = self.produce_node
        result['BizData'] = self.biz_data
        result['MetaInfo'] = self.meta_info
        result['CertifyPrincipal'] = self.certify_principal
        result['AppVersion'] = self.app_version
        result['DeviceToken'] = self.device_token
        result['UaToken'] = self.ua_token
        result['WebUmidToken'] = self.web_umid_token
        return result

    def from_map(self, map={}):
        self.certify_id = map.get('CertifyId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.channel = map.get('Channel')
        self.merchant = map.get('Merchant')
        self.product_name = map.get('ProductName')
        self.produce_node = map.get('ProduceNode')
        self.biz_data = map.get('BizData')
        self.meta_info = map.get('MetaInfo')
        self.certify_principal = map.get('CertifyPrincipal')
        self.app_version = map.get('AppVersion')
        self.device_token = map.get('DeviceToken')
        self.ua_token = map.get('UaToken')
        self.web_umid_token = map.get('WebUmidToken')
        return self


class InitDeviceResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: InitDeviceResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = InitDeviceResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class InitDeviceResponseResultObject(TeaModel):
    def __init__(self, certify_id=None, protocol=None, ext_params=None, ret_code=None, ret_code_sub=None,
                 ret_message_sub=None, message=None, oss_end_point=None, access_key_id=None, access_key_secret=None,
                 security_token=None, bucket_name=None, file_name_prefix=None, file_name=None, presigned_url=None):
        self.certify_id = certify_id    # type: str
        self.protocol = protocol        # type: str
        self.ext_params = ext_params    # type: str
        self.ret_code = ret_code        # type: str
        self.ret_code_sub = ret_code_sub  # type: str
        self.ret_message_sub = ret_message_sub  # type: str
        self.message = message          # type: str
        self.oss_end_point = oss_end_point  # type: str
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.security_token = security_token  # type: str
        self.bucket_name = bucket_name  # type: str
        self.file_name_prefix = file_name_prefix  # type: str
        self.file_name = file_name      # type: str
        self.presigned_url = presigned_url  # type: str

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.ext_params, 'ext_params')
        self.validate_required(self.ret_code, 'ret_code')
        self.validate_required(self.ret_code_sub, 'ret_code_sub')
        self.validate_required(self.ret_message_sub, 'ret_message_sub')
        self.validate_required(self.message, 'message')
        self.validate_required(self.oss_end_point, 'oss_end_point')
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.access_key_secret, 'access_key_secret')
        self.validate_required(self.security_token, 'security_token')
        self.validate_required(self.bucket_name, 'bucket_name')
        self.validate_required(self.file_name_prefix, 'file_name_prefix')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.presigned_url, 'presigned_url')

    def to_map(self):
        result = {}
        result['CertifyId'] = self.certify_id
        result['Protocol'] = self.protocol
        result['ExtParams'] = self.ext_params
        result['RetCode'] = self.ret_code
        result['RetCodeSub'] = self.ret_code_sub
        result['RetMessageSub'] = self.ret_message_sub
        result['Message'] = self.message
        result['OssEndPoint'] = self.oss_end_point
        result['AccessKeyId'] = self.access_key_id
        result['AccessKeySecret'] = self.access_key_secret
        result['SecurityToken'] = self.security_token
        result['BucketName'] = self.bucket_name
        result['FileNamePrefix'] = self.file_name_prefix
        result['FileName'] = self.file_name
        result['PresignedUrl'] = self.presigned_url
        return result

    def from_map(self, map={}):
        self.certify_id = map.get('CertifyId')
        self.protocol = map.get('Protocol')
        self.ext_params = map.get('ExtParams')
        self.ret_code = map.get('RetCode')
        self.ret_code_sub = map.get('RetCodeSub')
        self.ret_message_sub = map.get('RetMessageSub')
        self.message = map.get('Message')
        self.oss_end_point = map.get('OssEndPoint')
        self.access_key_id = map.get('AccessKeyId')
        self.access_key_secret = map.get('AccessKeySecret')
        self.security_token = map.get('SecurityToken')
        self.bucket_name = map.get('BucketName')
        self.file_name_prefix = map.get('FileNamePrefix')
        self.file_name = map.get('FileName')
        self.presigned_url = map.get('PresignedUrl')
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, outer_order_no=None, product_code=None, cert_type=None, cert_name=None,
                 cert_no=None, return_url=None, face_contrast_picture=None, meta_info=None, mobile=None, ip=None,
                 user_id=None, face_contrast_picture_url=None, certify_id=None, oss_bucket_name=None, oss_object_name=None,
                 model=None, callback_url=None, callback_token=None):
        self.scene_id = scene_id        # type: int
        self.outer_order_no = outer_order_no  # type: str
        self.product_code = product_code  # type: str
        self.cert_type = cert_type      # type: str
        self.cert_name = cert_name      # type: str
        self.cert_no = cert_no          # type: str
        self.return_url = return_url    # type: str
        self.face_contrast_picture = face_contrast_picture  # type: str
        self.meta_info = meta_info      # type: str
        self.mobile = mobile            # type: str
        self.ip = ip                    # type: str
        self.user_id = user_id          # type: str
        self.face_contrast_picture_url = face_contrast_picture_url  # type: str
        self.certify_id = certify_id    # type: str
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_name = oss_object_name  # type: str
        self.model = model              # type: str
        self.callback_url = callback_url  # type: str
        self.callback_token = callback_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['OuterOrderNo'] = self.outer_order_no
        result['ProductCode'] = self.product_code
        result['CertType'] = self.cert_type
        result['CertName'] = self.cert_name
        result['CertNo'] = self.cert_no
        result['ReturnUrl'] = self.return_url
        result['FaceContrastPicture'] = self.face_contrast_picture
        result['MetaInfo'] = self.meta_info
        result['Mobile'] = self.mobile
        result['Ip'] = self.ip
        result['UserId'] = self.user_id
        result['FaceContrastPictureUrl'] = self.face_contrast_picture_url
        result['CertifyId'] = self.certify_id
        result['OssBucketName'] = self.oss_bucket_name
        result['OssObjectName'] = self.oss_object_name
        result['Model'] = self.model
        result['CallbackUrl'] = self.callback_url
        result['CallbackToken'] = self.callback_token
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.outer_order_no = map.get('OuterOrderNo')
        self.product_code = map.get('ProductCode')
        self.cert_type = map.get('CertType')
        self.cert_name = map.get('CertName')
        self.cert_no = map.get('CertNo')
        self.return_url = map.get('ReturnUrl')
        self.face_contrast_picture = map.get('FaceContrastPicture')
        self.meta_info = map.get('MetaInfo')
        self.mobile = map.get('Mobile')
        self.ip = map.get('Ip')
        self.user_id = map.get('UserId')
        self.face_contrast_picture_url = map.get('FaceContrastPictureUrl')
        self.certify_id = map.get('CertifyId')
        self.oss_bucket_name = map.get('OssBucketName')
        self.oss_object_name = map.get('OssObjectName')
        self.model = map.get('Model')
        self.callback_url = map.get('CallbackUrl')
        self.callback_token = map.get('CallbackToken')
        return self


class InitFaceVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: InitFaceVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = InitFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class InitFaceVerifyResponseResultObject(TeaModel):
    def __init__(self, certify_id=None, certify_url=None):
        self.certify_id = certify_id    # type: str
        self.certify_url = certify_url  # type: str

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.certify_url, 'certify_url')

    def to_map(self):
        result = {}
        result['CertifyId'] = self.certify_id
        result['CertifyUrl'] = self.certify_url
        return result

    def from_map(self, map={}):
        self.certify_id = map.get('CertifyId')
        self.certify_url = map.get('CertifyUrl')
        return self


class DescribeFaceVerifyRequest(TeaModel):
    def __init__(self, scene_id=None, certify_id=None):
        self.scene_id = scene_id        # type: int
        self.certify_id = certify_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['CertifyId'] = self.certify_id
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.certify_id = map.get('CertifyId')
        return self


class DescribeFaceVerifyResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, result_object=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.result_object = result_object  # type: DescribeFaceVerifyResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        if map.get('ResultObject') is not None:
            temp_model = DescribeFaceVerifyResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class DescribeFaceVerifyResponseResultObject(TeaModel):
    def __init__(self, passed=None, identity_info=None, material_info=None, device_token=None, sub_code=None):
        self.passed = passed            # type: str
        self.identity_info = identity_info  # type: str
        self.material_info = material_info  # type: str
        self.device_token = device_token  # type: str
        self.sub_code = sub_code        # type: str

    def validate(self):
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.identity_info, 'identity_info')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.device_token, 'device_token')
        self.validate_required(self.sub_code, 'sub_code')

    def to_map(self):
        result = {}
        result['Passed'] = self.passed
        result['IdentityInfo'] = self.identity_info
        result['MaterialInfo'] = self.material_info
        result['DeviceToken'] = self.device_token
        result['SubCode'] = self.sub_code
        return result

    def from_map(self, map={}):
        self.passed = map.get('Passed')
        self.identity_info = map.get('IdentityInfo')
        self.material_info = map.get('MaterialInfo')
        self.device_token = map.get('DeviceToken')
        self.sub_code = map.get('SubCode')
        return self


class VerifyDeviceRequest(TeaModel):
    def __init__(self, certify_id=None, certify_data=None, app_version=None, ext_info=None):
        self.certify_id = certify_id    # type: str
        self.certify_data = certify_data  # type: str
        self.app_version = app_version  # type: str
        self.ext_info = ext_info        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CertifyId'] = self.certify_id
        result['CertifyData'] = self.certify_data
        result['AppVersion'] = self.app_version
        result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, map={}):
        self.certify_id = map.get('CertifyId')
        self.certify_data = map.get('CertifyData')
        self.app_version = map.get('AppVersion')
        self.ext_info = map.get('ExtInfo')
        return self


class VerifyDeviceResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result_object=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.result_object = result_object  # type: VerifyDeviceResponseResultObject

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('ResultObject') is not None:
            temp_model = VerifyDeviceResponseResultObject()
            self.result_object = temp_model.from_map(map['ResultObject'])
        else:
            self.result_object = None
        return self


class VerifyDeviceResponseResultObject(TeaModel):
    def __init__(self, validation_ret_code=None, product_ret_code=None, ret_code_sub=None, ret_message_sub=None,
                 has_next=None, ext_params=None):
        self.validation_ret_code = validation_ret_code  # type: str
        self.product_ret_code = product_ret_code  # type: str
        self.ret_code_sub = ret_code_sub  # type: str
        self.ret_message_sub = ret_message_sub  # type: str
        self.has_next = has_next        # type: str
        self.ext_params = ext_params    # type: str

    def validate(self):
        self.validate_required(self.validation_ret_code, 'validation_ret_code')
        self.validate_required(self.product_ret_code, 'product_ret_code')
        self.validate_required(self.ret_code_sub, 'ret_code_sub')
        self.validate_required(self.ret_message_sub, 'ret_message_sub')
        self.validate_required(self.has_next, 'has_next')
        self.validate_required(self.ext_params, 'ext_params')

    def to_map(self):
        result = {}
        result['ValidationRetCode'] = self.validation_ret_code
        result['ProductRetCode'] = self.product_ret_code
        result['RetCodeSub'] = self.ret_code_sub
        result['RetMessageSub'] = self.ret_message_sub
        result['HasNext'] = self.has_next
        result['ExtParams'] = self.ext_params
        return result

    def from_map(self, map={}):
        self.validation_ret_code = map.get('ValidationRetCode')
        self.product_ret_code = map.get('ProductRetCode')
        self.ret_code_sub = map.get('RetCodeSub')
        self.ret_message_sub = map.get('RetMessageSub')
        self.has_next = map.get('HasNext')
        self.ext_params = map.get('ExtParams')
        return self


class ModifyDeviceInfoRequest(TeaModel):
    def __init__(self, device_id=None, user_device_id=None, biz_type=None, duration=None, expired_day=None):
        self.device_id = device_id      # type: str
        self.user_device_id = user_device_id  # type: str
        self.biz_type = biz_type        # type: str
        self.duration = duration        # type: str
        self.expired_day = expired_day  # type: str

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        result = {}
        result['DeviceId'] = self.device_id
        result['UserDeviceId'] = self.user_device_id
        result['BizType'] = self.biz_type
        result['Duration'] = self.duration
        result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, map={}):
        self.device_id = map.get('DeviceId')
        self.user_device_id = map.get('UserDeviceId')
        self.biz_type = map.get('BizType')
        self.duration = map.get('Duration')
        self.expired_day = map.get('ExpiredDay')
        return self


class ModifyDeviceInfoResponse(TeaModel):
    def __init__(self, request_id=None, device_id=None, user_device_id=None, biz_type=None, begin_day=None,
                 expired_day=None):
        self.request_id = request_id    # type: str
        self.device_id = device_id      # type: str
        self.user_device_id = user_device_id  # type: str
        self.biz_type = biz_type        # type: str
        self.begin_day = begin_day      # type: str
        self.expired_day = expired_day  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_device_id, 'user_device_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.begin_day, 'begin_day')
        self.validate_required(self.expired_day, 'expired_day')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DeviceId'] = self.device_id
        result['UserDeviceId'] = self.user_device_id
        result['BizType'] = self.biz_type
        result['BeginDay'] = self.begin_day
        result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.device_id = map.get('DeviceId')
        self.user_device_id = map.get('UserDeviceId')
        self.biz_type = map.get('BizType')
        self.begin_day = map.get('BeginDay')
        self.expired_day = map.get('ExpiredDay')
        return self


class DescribeVerifySDKRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        return self


class DescribeVerifySDKResponse(TeaModel):
    def __init__(self, request_id=None, sdk_url=None):
        self.request_id = request_id    # type: str
        self.sdk_url = sdk_url          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sdk_url, 'sdk_url')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.sdk_url = map.get('SdkUrl')
        return self


class DescribeDeviceInfoRequest(TeaModel):
    def __init__(self, page_size=None, current_page=None, device_id=None, biz_type=None, user_device_id=None,
                 expired_start_day=None, expired_end_day=None):
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.device_id = device_id      # type: str
        self.biz_type = biz_type        # type: str
        self.user_device_id = user_device_id  # type: str
        self.expired_start_day = expired_start_day  # type: str
        self.expired_end_day = expired_end_day  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['DeviceId'] = self.device_id
        result['BizType'] = self.biz_type
        result['UserDeviceId'] = self.user_device_id
        result['ExpiredStartDay'] = self.expired_start_day
        result['ExpiredEndDay'] = self.expired_end_day
        return result

    def from_map(self, map={}):
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.device_id = map.get('DeviceId')
        self.biz_type = map.get('BizType')
        self.user_device_id = map.get('UserDeviceId')
        self.expired_start_day = map.get('ExpiredStartDay')
        self.expired_end_day = map.get('ExpiredEndDay')
        return self


class DescribeDeviceInfoResponse(TeaModel):
    def __init__(self, request_id=None, page_size=None, current_page=None, total_count=None, device_info_list=None):
        self.request_id = request_id    # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.total_count = total_count  # type: int
        self.device_info_list = device_info_list  # type: DescribeDeviceInfoResponseDeviceInfoList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.device_info_list, 'device_info_list')
        if self.device_info_list:
            self.device_info_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['TotalCount'] = self.total_count
        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()
        else:
            result['DeviceInfoList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.total_count = map.get('TotalCount')
        if map.get('DeviceInfoList') is not None:
            temp_model = DescribeDeviceInfoResponseDeviceInfoList()
            self.device_info_list = temp_model.from_map(map['DeviceInfoList'])
        else:
            self.device_info_list = None
        return self


class DescribeDeviceInfoResponseDeviceInfoListDeviceInfo(TeaModel):
    def __init__(self, device_id=None, user_device_id=None, biz_type=None, begin_day=None, expired_day=None):
        self.device_id = device_id      # type: str
        self.user_device_id = user_device_id  # type: str
        self.biz_type = biz_type        # type: str
        self.begin_day = begin_day      # type: str
        self.expired_day = expired_day  # type: str

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_device_id, 'user_device_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.begin_day, 'begin_day')
        self.validate_required(self.expired_day, 'expired_day')

    def to_map(self):
        result = {}
        result['DeviceId'] = self.device_id
        result['UserDeviceId'] = self.user_device_id
        result['BizType'] = self.biz_type
        result['BeginDay'] = self.begin_day
        result['ExpiredDay'] = self.expired_day
        return result

    def from_map(self, map={}):
        self.device_id = map.get('DeviceId')
        self.user_device_id = map.get('UserDeviceId')
        self.biz_type = map.get('BizType')
        self.begin_day = map.get('BeginDay')
        self.expired_day = map.get('ExpiredDay')
        return self


class DescribeDeviceInfoResponseDeviceInfoList(TeaModel):
    def __init__(self, device_info=None):
        self.device_info = device_info  # type: List[DescribeDeviceInfoResponseDeviceInfoListDeviceInfo]

    def validate(self):
        self.validate_required(self.device_info, 'device_info')
        if self.device_info:
            for k in self.device_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DeviceInfo'] = []
        if self.device_info is not None:
            for k in self.device_info:
                result['DeviceInfo'].append(k.to_map() if k else None)
        else:
            result['DeviceInfo'] = None
        return result

    def from_map(self, map={}):
        self.device_info = []
        if map.get('DeviceInfo') is not None:
            for k in map.get('DeviceInfo'):
                temp_model = DescribeDeviceInfoResponseDeviceInfoListDeviceInfo()
                self.device_info.append(temp_model.from_map(k))
        else:
            self.device_info = None
        return self


class CreateVerifySDKRequest(TeaModel):
    def __init__(self, app_url=None, platform=None):
        self.app_url = app_url          # type: str
        self.platform = platform        # type: str

    def validate(self):
        self.validate_required(self.app_url, 'app_url')

    def to_map(self):
        result = {}
        result['AppUrl'] = self.app_url
        result['Platform'] = self.platform
        return result

    def from_map(self, map={}):
        self.app_url = map.get('AppUrl')
        self.platform = map.get('Platform')
        return self


class CreateVerifySDKResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class CreateAuthKeyRequest(TeaModel):
    def __init__(self, biz_type=None, user_device_id=None, test=None, auth_years=None):
        self.biz_type = biz_type        # type: str
        self.user_device_id = user_device_id  # type: str
        self.test = test                # type: bool
        self.auth_years = auth_years    # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['UserDeviceId'] = self.user_device_id
        result['Test'] = self.test
        result['AuthYears'] = self.auth_years
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.user_device_id = map.get('UserDeviceId')
        self.test = map.get('Test')
        self.auth_years = map.get('AuthYears')
        return self


class CreateAuthKeyResponse(TeaModel):
    def __init__(self, request_id=None, auth_key=None):
        self.request_id = request_id    # type: str
        self.auth_key = auth_key        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.auth_key, 'auth_key')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AuthKey'] = self.auth_key
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.auth_key = map.get('AuthKey')
        return self


class DetectFaceAttributesRequest(TeaModel):
    def __init__(self, material_value=None, biz_type=None):
        self.material_value = material_value  # type: str
        self.biz_type = biz_type        # type: str

    def validate(self):
        self.validate_required(self.material_value, 'material_value')

    def to_map(self):
        result = {}
        result['MaterialValue'] = self.material_value
        result['BizType'] = self.biz_type
        return result

    def from_map(self, map={}):
        self.material_value = map.get('MaterialValue')
        self.biz_type = map.get('BizType')
        return self


class DetectFaceAttributesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: DetectFaceAttributesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = DetectFaceAttributesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceRect(TeaModel):
    def __init__(self, top=None, left=None, width=None, height=None):
        self.top = top                  # type: int
        self.left = left                # type: int
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.top, 'top')
        self.validate_required(self.left, 'left')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        result['Top'] = self.top
        result['Left'] = self.left
        result['Width'] = self.width
        result['Height'] = self.height
        return result

    def from_map(self, map={}):
        self.top = map.get('Top')
        self.left = map.get('Left')
        self.width = map.get('Width')
        self.height = map.get('Height')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesGender(TeaModel):
    def __init__(self, score=None, value=None):
        self.score = score              # type: float
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.score, 'score')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Score'] = self.score
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.score = map.get('Score')
        self.value = map.get('Value')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling(TeaModel):
    def __init__(self, value=None, threshold=None):
        self.value = value              # type: float
        self.threshold = threshold      # type: float

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.threshold, 'threshold')

    def to_map(self):
        result = {}
        result['Value'] = self.value
        result['Threshold'] = self.threshold
        return result

    def from_map(self, map={}):
        self.value = map.get('Value')
        self.threshold = map.get('Threshold')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose(TeaModel):
    def __init__(self, pitch_angle=None, roll_angle=None, yaw_angle=None):
        self.pitch_angle = pitch_angle  # type: float
        self.roll_angle = roll_angle    # type: float
        self.yaw_angle = yaw_angle      # type: float

    def validate(self):
        self.validate_required(self.pitch_angle, 'pitch_angle')
        self.validate_required(self.roll_angle, 'roll_angle')
        self.validate_required(self.yaw_angle, 'yaw_angle')

    def to_map(self):
        result = {}
        result['PitchAngle'] = self.pitch_angle
        result['RollAngle'] = self.roll_angle
        result['YawAngle'] = self.yaw_angle
        return result

    def from_map(self, map={}):
        self.pitch_angle = map.get('PitchAngle')
        self.roll_angle = map.get('RollAngle')
        self.yaw_angle = map.get('YawAngle')
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributes(TeaModel):
    def __init__(self, age=None, glasses=None, facetype=None, blur=None, ethnicity=None, gender=None, smiling=None,
                 headpose=None):
        self.age = age                  # type: int
        self.glasses = glasses          # type: str
        self.facetype = facetype        # type: str
        self.blur = blur                # type: float
        self.ethnicity = ethnicity      # type: str
        self.gender = gender            # type: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesGender
        self.smiling = smiling          # type: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling
        self.headpose = headpose        # type: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose

    def validate(self):
        self.validate_required(self.age, 'age')
        self.validate_required(self.glasses, 'glasses')
        self.validate_required(self.facetype, 'facetype')
        self.validate_required(self.blur, 'blur')
        self.validate_required(self.ethnicity, 'ethnicity')
        self.validate_required(self.gender, 'gender')
        if self.gender:
            self.gender.validate()
        self.validate_required(self.smiling, 'smiling')
        if self.smiling:
            self.smiling.validate()
        self.validate_required(self.headpose, 'headpose')
        if self.headpose:
            self.headpose.validate()

    def to_map(self):
        result = {}
        result['Age'] = self.age
        result['Glasses'] = self.glasses
        result['Facetype'] = self.facetype
        result['Blur'] = self.blur
        result['Ethnicity'] = self.ethnicity
        if self.gender is not None:
            result['Gender'] = self.gender.to_map()
        else:
            result['Gender'] = None
        if self.smiling is not None:
            result['Smiling'] = self.smiling.to_map()
        else:
            result['Smiling'] = None
        if self.headpose is not None:
            result['Headpose'] = self.headpose.to_map()
        else:
            result['Headpose'] = None
        return result

    def from_map(self, map={}):
        self.age = map.get('Age')
        self.glasses = map.get('Glasses')
        self.facetype = map.get('Facetype')
        self.blur = map.get('Blur')
        self.ethnicity = map.get('Ethnicity')
        if map.get('Gender') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesGender()
            self.gender = temp_model.from_map(map['Gender'])
        else:
            self.gender = None
        if map.get('Smiling') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesSmiling()
            self.smiling = temp_model.from_map(map['Smiling'])
        else:
            self.smiling = None
        if map.get('Headpose') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributesHeadpose()
            self.headpose = temp_model.from_map(map['Headpose'])
        else:
            self.headpose = None
        return self


class DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfo(TeaModel):
    def __init__(self, face_rect=None, face_attributes=None):
        self.face_rect = face_rect      # type: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceRect
        self.face_attributes = face_attributes  # type: DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributes

    def validate(self):
        self.validate_required(self.face_rect, 'face_rect')
        if self.face_rect:
            self.face_rect.validate()
        self.validate_required(self.face_attributes, 'face_attributes')
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        result = {}
        if self.face_rect is not None:
            result['FaceRect'] = self.face_rect.to_map()
        else:
            result['FaceRect'] = None
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        else:
            result['FaceAttributes'] = None
        return result

    def from_map(self, map={}):
        if map.get('FaceRect') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceRect()
            self.face_rect = temp_model.from_map(map['FaceRect'])
        else:
            self.face_rect = None
        if map.get('FaceAttributes') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfoFaceAttributes()
            self.face_attributes = temp_model.from_map(map['FaceAttributes'])
        else:
            self.face_attributes = None
        return self


class DetectFaceAttributesResponseDataFaceInfos(TeaModel):
    def __init__(self, face_attributes_detect_info=None):
        self.face_attributes_detect_info = face_attributes_detect_info  # type: List[DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfo]

    def validate(self):
        self.validate_required(self.face_attributes_detect_info, 'face_attributes_detect_info')
        if self.face_attributes_detect_info:
            for k in self.face_attributes_detect_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FaceAttributesDetectInfo'] = []
        if self.face_attributes_detect_info is not None:
            for k in self.face_attributes_detect_info:
                result['FaceAttributesDetectInfo'].append(k.to_map() if k else None)
        else:
            result['FaceAttributesDetectInfo'] = None
        return result

    def from_map(self, map={}):
        self.face_attributes_detect_info = []
        if map.get('FaceAttributesDetectInfo') is not None:
            for k in map.get('FaceAttributesDetectInfo'):
                temp_model = DetectFaceAttributesResponseDataFaceInfosFaceAttributesDetectInfo()
                self.face_attributes_detect_info.append(temp_model.from_map(k))
        else:
            self.face_attributes_detect_info = None
        return self


class DetectFaceAttributesResponseData(TeaModel):
    def __init__(self, img_width=None, img_height=None, face_infos=None):
        self.img_width = img_width      # type: int
        self.img_height = img_height    # type: int
        self.face_infos = face_infos    # type: DetectFaceAttributesResponseDataFaceInfos

    def validate(self):
        self.validate_required(self.img_width, 'img_width')
        self.validate_required(self.img_height, 'img_height')
        self.validate_required(self.face_infos, 'face_infos')
        if self.face_infos:
            self.face_infos.validate()

    def to_map(self):
        result = {}
        result['ImgWidth'] = self.img_width
        result['ImgHeight'] = self.img_height
        if self.face_infos is not None:
            result['FaceInfos'] = self.face_infos.to_map()
        else:
            result['FaceInfos'] = None
        return result

    def from_map(self, map={}):
        self.img_width = map.get('ImgWidth')
        self.img_height = map.get('ImgHeight')
        if map.get('FaceInfos') is not None:
            temp_model = DetectFaceAttributesResponseDataFaceInfos()
            self.face_infos = temp_model.from_map(map['FaceInfos'])
        else:
            self.face_infos = None
        return self


class CompareFacesRequest(TeaModel):
    def __init__(self, target_image_type=None, source_image_type=None, source_image_value=None,
                 target_image_value=None, biz_type=None):
        self.target_image_type = target_image_type  # type: str
        self.source_image_type = source_image_type  # type: str
        self.source_image_value = source_image_value  # type: str
        self.target_image_value = target_image_value  # type: str
        self.biz_type = biz_type        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['TargetImageType'] = self.target_image_type
        result['SourceImageType'] = self.source_image_type
        result['SourceImageValue'] = self.source_image_value
        result['TargetImageValue'] = self.target_image_value
        result['BizType'] = self.biz_type
        return result

    def from_map(self, map={}):
        self.target_image_type = map.get('TargetImageType')
        self.source_image_type = map.get('SourceImageType')
        self.source_image_value = map.get('SourceImageValue')
        self.target_image_value = map.get('TargetImageValue')
        self.biz_type = map.get('BizType')
        return self


class CompareFacesResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: CompareFacesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = CompareFacesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CompareFacesResponseData(TeaModel):
    def __init__(self, similarity_score=None, confidence_thresholds=None):
        self.similarity_score = similarity_score  # type: float
        self.confidence_thresholds = confidence_thresholds  # type: str

    def validate(self):
        self.validate_required(self.similarity_score, 'similarity_score')
        self.validate_required(self.confidence_thresholds, 'confidence_thresholds')

    def to_map(self):
        result = {}
        result['SimilarityScore'] = self.similarity_score
        result['ConfidenceThresholds'] = self.confidence_thresholds
        return result

    def from_map(self, map={}):
        self.similarity_score = map.get('SimilarityScore')
        self.confidence_thresholds = map.get('ConfidenceThresholds')
        return self


class DescribeFaceUsageRequest(TeaModel):
    def __init__(self, start_date=None, end_date=None):
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class DescribeFaceUsageResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, face_usage_list=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.face_usage_list = face_usage_list  # type: List[DescribeFaceUsageResponseFaceUsageList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.face_usage_list, 'face_usage_list')
        if self.face_usage_list:
            for k in self.face_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['FaceUsageList'] = []
        if self.face_usage_list is not None:
            for k in self.face_usage_list:
                result['FaceUsageList'].append(k.to_map() if k else None)
        else:
            result['FaceUsageList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.face_usage_list = []
        if map.get('FaceUsageList') is not None:
            for k in map.get('FaceUsageList'):
                temp_model = DescribeFaceUsageResponseFaceUsageList()
                self.face_usage_list.append(temp_model.from_map(k))
        else:
            self.face_usage_list = None
        return self


class DescribeFaceUsageResponseFaceUsageList(TeaModel):
    def __init__(self, date=None, total_count=None):
        self.date = date                # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.total_count, 'total_count')

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['TotalCount'] = self.total_count
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.total_count = map.get('TotalCount')
        return self


class DescribeVerifyRecordsRequest(TeaModel):
    def __init__(self, total_count=None, page_size=None, current_page=None, biz_type=None, start_date=None,
                 end_date=None, biz_id=None, id_card_num=None, status_list=None, query_id=None):
        self.total_count = total_count  # type: int
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.biz_type = biz_type        # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.biz_id = biz_id            # type: str
        self.id_card_num = id_card_num  # type: str
        self.status_list = status_list  # type: str
        self.query_id = query_id        # type: str

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['BizType'] = self.biz_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['BizId'] = self.biz_id
        result['IdCardNum'] = self.id_card_num
        result['StatusList'] = self.status_list
        result['QueryId'] = self.query_id
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.biz_type = map.get('BizType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.biz_id = map.get('BizId')
        self.id_card_num = map.get('IdCardNum')
        self.status_list = map.get('StatusList')
        self.query_id = map.get('QueryId')
        return self


class DescribeVerifyRecordsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_size=None, current_page=None, query_id=None,
                 records_list=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.query_id = query_id        # type: str
        self.records_list = records_list  # type: List[DescribeVerifyRecordsResponseRecordsList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.query_id, 'query_id')
        self.validate_required(self.records_list, 'records_list')
        if self.records_list:
            for k in self.records_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['QueryId'] = self.query_id
        result['RecordsList'] = []
        if self.records_list is not None:
            for k in self.records_list:
                result['RecordsList'].append(k.to_map() if k else None)
        else:
            result['RecordsList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.query_id = map.get('QueryId')
        self.records_list = []
        if map.get('RecordsList') is not None:
            for k in map.get('RecordsList'):
                temp_model = DescribeVerifyRecordsResponseRecordsList()
                self.records_list.append(temp_model.from_map(k))
        else:
            self.records_list = None
        return self


class DescribeVerifyRecordsResponseRecordsListMaterialIdCardInfo(TeaModel):
    def __init__(self, front_image_url=None, back_image_url=None, name=None, number=None, address=None, birth=None,
                 sex=None, nationality=None, authority=None, start_date=None, end_date=None):
        self.front_image_url = front_image_url  # type: str
        self.back_image_url = back_image_url  # type: str
        self.name = name                # type: str
        self.number = number            # type: str
        self.address = address          # type: str
        self.birth = birth              # type: str
        self.sex = sex                  # type: str
        self.nationality = nationality  # type: str
        self.authority = authority      # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.front_image_url, 'front_image_url')
        self.validate_required(self.back_image_url, 'back_image_url')
        self.validate_required(self.name, 'name')
        self.validate_required(self.number, 'number')
        self.validate_required(self.address, 'address')
        self.validate_required(self.birth, 'birth')
        self.validate_required(self.sex, 'sex')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['FrontImageUrl'] = self.front_image_url
        result['BackImageUrl'] = self.back_image_url
        result['Name'] = self.name
        result['Number'] = self.number
        result['Address'] = self.address
        result['Birth'] = self.birth
        result['Sex'] = self.sex
        result['Nationality'] = self.nationality
        result['Authority'] = self.authority
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.front_image_url = map.get('FrontImageUrl')
        self.back_image_url = map.get('BackImageUrl')
        self.name = map.get('Name')
        self.number = map.get('Number')
        self.address = map.get('Address')
        self.birth = map.get('Birth')
        self.sex = map.get('Sex')
        self.nationality = map.get('Nationality')
        self.authority = map.get('Authority')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class DescribeVerifyRecordsResponseRecordsListMaterial(TeaModel):
    def __init__(self, face_image_url=None, id_card_name=None, id_card_number=None, id_card_info=None):
        self.face_image_url = face_image_url  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_info = id_card_info  # type: DescribeVerifyRecordsResponseRecordsListMaterialIdCardInfo

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.id_card_name, 'id_card_name')
        self.validate_required(self.id_card_number, 'id_card_number')
        self.validate_required(self.id_card_info, 'id_card_info')
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        result = {}
        result['FaceImageUrl'] = self.face_image_url
        result['IdCardName'] = self.id_card_name
        result['IdCardNumber'] = self.id_card_number
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        else:
            result['IdCardInfo'] = None
        return result

    def from_map(self, map={}):
        self.face_image_url = map.get('FaceImageUrl')
        self.id_card_name = map.get('IdCardName')
        self.id_card_number = map.get('IdCardNumber')
        if map.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyRecordsResponseRecordsListMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(map['IdCardInfo'])
        else:
            self.id_card_info = None
        return self


class DescribeVerifyRecordsResponseRecordsList(TeaModel):
    def __init__(self, biz_type=None, biz_id=None, data_stats=None, verify_id=None, finish_time=None, status=None,
                 id_card_face_comparison_score=None, authority_comparison_score=None, material=None):
        self.biz_type = biz_type        # type: str
        self.biz_id = biz_id            # type: str
        self.data_stats = data_stats    # type: str
        self.verify_id = verify_id      # type: str
        self.finish_time = finish_time  # type: int
        self.status = status            # type: int
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.authority_comparison_score = authority_comparison_score  # type: float
        self.material = material        # type: DescribeVerifyRecordsResponseRecordsListMaterial

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.data_stats, 'data_stats')
        self.validate_required(self.verify_id, 'verify_id')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.id_card_face_comparison_score, 'id_card_face_comparison_score')
        self.validate_required(self.authority_comparison_score, 'authority_comparison_score')
        self.validate_required(self.material, 'material')
        if self.material:
            self.material.validate()

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['BizId'] = self.biz_id
        result['DataStats'] = self.data_stats
        result['VerifyId'] = self.verify_id
        result['FinishTime'] = self.finish_time
        result['Status'] = self.status
        result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        result['AuthorityComparisonScore'] = self.authority_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        else:
            result['Material'] = None
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.biz_id = map.get('BizId')
        self.data_stats = map.get('DataStats')
        self.verify_id = map.get('VerifyId')
        self.finish_time = map.get('FinishTime')
        self.status = map.get('Status')
        self.id_card_face_comparison_score = map.get('IdCardFaceComparisonScore')
        self.authority_comparison_score = map.get('AuthorityComparisonScore')
        if map.get('Material') is not None:
            temp_model = DescribeVerifyRecordsResponseRecordsListMaterial()
            self.material = temp_model.from_map(map['Material'])
        else:
            self.material = None
        return self


class UpdateVerifySettingRequest(TeaModel):
    def __init__(self, biz_type=None, biz_name=None, solution=None, guide_step=None, privacy_step=None,
                 result_step=None):
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str
        self.solution = solution        # type: str
        self.guide_step = guide_step    # type: bool
        self.privacy_step = privacy_step  # type: bool
        self.result_step = result_step  # type: bool

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        result['Solution'] = self.solution
        result['GuideStep'] = self.guide_step
        result['PrivacyStep'] = self.privacy_step
        result['ResultStep'] = self.result_step
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        self.solution = map.get('Solution')
        self.guide_step = map.get('GuideStep')
        self.privacy_step = map.get('PrivacyStep')
        self.result_step = map.get('ResultStep')
        return self


class UpdateVerifySettingResponse(TeaModel):
    def __init__(self, request_id=None, biz_type=None, biz_name=None, solution=None, step_list=None):
        self.request_id = request_id    # type: str
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str
        self.solution = solution        # type: str
        self.step_list = step_list      # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')
        self.validate_required(self.step_list, 'step_list')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        result['Solution'] = self.solution
        result['StepList'] = self.step_list
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        self.solution = map.get('Solution')
        self.step_list = map.get('StepList')
        return self


class CreateVerifySettingRequest(TeaModel):
    def __init__(self, biz_type=None, biz_name=None, solution=None, guide_step=None, privacy_step=None,
                 result_step=None):
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str
        self.solution = solution        # type: str
        self.guide_step = guide_step    # type: bool
        self.privacy_step = privacy_step  # type: bool
        self.result_step = result_step  # type: bool

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        result['Solution'] = self.solution
        result['GuideStep'] = self.guide_step
        result['PrivacyStep'] = self.privacy_step
        result['ResultStep'] = self.result_step
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        self.solution = map.get('Solution')
        self.guide_step = map.get('GuideStep')
        self.privacy_step = map.get('PrivacyStep')
        self.result_step = map.get('ResultStep')
        return self


class CreateVerifySettingResponse(TeaModel):
    def __init__(self, request_id=None, biz_type=None, biz_name=None, solution=None, step_list=None):
        self.request_id = request_id    # type: str
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str
        self.solution = solution        # type: str
        self.step_list = step_list      # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')
        self.validate_required(self.step_list, 'step_list')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        result['Solution'] = self.solution
        result['StepList'] = self.step_list
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        self.solution = map.get('Solution')
        self.step_list = map.get('StepList')
        return self


class DescribeVerifySettingRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeVerifySettingResponse(TeaModel):
    def __init__(self, request_id=None, verify_setting_list=None):
        self.request_id = request_id    # type: str
        self.verify_setting_list = verify_setting_list  # type: List[DescribeVerifySettingResponseVerifySettingList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_setting_list, 'verify_setting_list')
        if self.verify_setting_list:
            for k in self.verify_setting_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VerifySettingList'] = []
        if self.verify_setting_list is not None:
            for k in self.verify_setting_list:
                result['VerifySettingList'].append(k.to_map() if k else None)
        else:
            result['VerifySettingList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.verify_setting_list = []
        if map.get('VerifySettingList') is not None:
            for k in map.get('VerifySettingList'):
                temp_model = DescribeVerifySettingResponseVerifySettingList()
                self.verify_setting_list.append(temp_model.from_map(k))
        else:
            self.verify_setting_list = None
        return self


class DescribeVerifySettingResponseVerifySettingList(TeaModel):
    def __init__(self, biz_type=None, biz_name=None, solution=None, step_list=None):
        self.biz_type = biz_type        # type: str
        self.biz_name = biz_name        # type: str
        self.solution = solution        # type: str
        self.step_list = step_list      # type: List[str]

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_name, 'biz_name')
        self.validate_required(self.solution, 'solution')
        self.validate_required(self.step_list, 'step_list')

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['BizName'] = self.biz_name
        result['Solution'] = self.solution
        result['StepList'] = self.step_list
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.biz_name = map.get('BizName')
        self.solution = map.get('Solution')
        self.step_list = map.get('StepList')
        return self


class DescribeVerifyUsageRequest(TeaModel):
    def __init__(self, biz_type=None, start_date=None, end_date=None):
        self.biz_type = biz_type        # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class DescribeVerifyUsageResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, verify_usage_list=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.verify_usage_list = verify_usage_list  # type: List[DescribeVerifyUsageResponseVerifyUsageList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.verify_usage_list, 'verify_usage_list')
        if self.verify_usage_list:
            for k in self.verify_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['VerifyUsageList'] = []
        if self.verify_usage_list is not None:
            for k in self.verify_usage_list:
                result['VerifyUsageList'].append(k.to_map() if k else None)
        else:
            result['VerifyUsageList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.verify_usage_list = []
        if map.get('VerifyUsageList') is not None:
            for k in map.get('VerifyUsageList'):
                temp_model = DescribeVerifyUsageResponseVerifyUsageList()
                self.verify_usage_list.append(temp_model.from_map(k))
        else:
            self.verify_usage_list = None
        return self


class DescribeVerifyUsageResponseVerifyUsageList(TeaModel):
    def __init__(self, biz_type=None, date=None, total_count=None, pass_count=None, fail_count=None):
        self.biz_type = biz_type        # type: str
        self.date = date                # type: str
        self.total_count = total_count  # type: int
        self.pass_count = pass_count    # type: int
        self.fail_count = fail_count    # type: int

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.date, 'date')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pass_count, 'pass_count')
        self.validate_required(self.fail_count, 'fail_count')

    def to_map(self):
        result = {}
        result['BizType'] = self.biz_type
        result['Date'] = self.date
        result['TotalCount'] = self.total_count
        result['PassCount'] = self.pass_count
        result['FailCount'] = self.fail_count
        return result

    def from_map(self, map={}):
        self.biz_type = map.get('BizType')
        self.date = map.get('Date')
        self.total_count = map.get('TotalCount')
        self.pass_count = map.get('PassCount')
        self.fail_count = map.get('FailCount')
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(self, request_id=None, enabled=None):
        self.request_id = request_id    # type: str
        self.enabled = enabled          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Enabled'] = self.enabled
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.enabled = map.get('Enabled')
        return self


class DescribeUploadInfoRequest(TeaModel):
    def __init__(self, biz=None):
        self.biz = biz                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Biz'] = self.biz
        return result

    def from_map(self, map={}):
        self.biz = map.get('Biz')
        return self


class DescribeUploadInfoResponse(TeaModel):
    def __init__(self, request_id=None, accessid=None, policy=None, signature=None, folder=None, host=None,
                 expire=None):
        self.request_id = request_id    # type: str
        self.accessid = accessid        # type: str
        self.policy = policy            # type: str
        self.signature = signature      # type: str
        self.folder = folder            # type: str
        self.host = host                # type: str
        self.expire = expire            # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.accessid, 'accessid')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.signature, 'signature')
        self.validate_required(self.folder, 'folder')
        self.validate_required(self.host, 'host')
        self.validate_required(self.expire, 'expire')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Accessid'] = self.accessid
        result['Policy'] = self.policy
        result['Signature'] = self.signature
        result['Folder'] = self.folder
        result['Host'] = self.host
        result['Expire'] = self.expire
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.accessid = map.get('Accessid')
        self.policy = map.get('Policy')
        self.signature = map.get('Signature')
        self.folder = map.get('Folder')
        self.host = map.get('Host')
        self.expire = map.get('Expire')
        return self


class DescribeRPSDKRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, task_id=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['Lang'] = self.lang
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.lang = map.get('Lang')
        self.task_id = map.get('TaskId')
        return self


class DescribeRPSDKResponse(TeaModel):
    def __init__(self, request_id=None, sdk_url=None):
        self.request_id = request_id    # type: str
        self.sdk_url = sdk_url          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sdk_url, 'sdk_url')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.sdk_url = map.get('SdkUrl')
        return self


class CreateRPSDKRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, app_url=None, platform=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.app_url = app_url          # type: str
        self.platform = platform        # type: str

    def validate(self):
        self.validate_required(self.app_url, 'app_url')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['Lang'] = self.lang
        result['AppUrl'] = self.app_url
        result['Platform'] = self.platform
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.lang = map.get('Lang')
        self.app_url = map.get('AppUrl')
        self.platform = map.get('Platform')
        return self


class CreateRPSDKResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class VerifyMaterialRequest(TeaModel):
    def __init__(self, id_card_back_image_url=None, face_image_url=None, biz_type=None, biz_id=None, name=None,
                 id_card_number=None, id_card_front_image_url=None, user_id=None):
        self.id_card_back_image_url = id_card_back_image_url  # type: str
        self.face_image_url = face_image_url  # type: str
        self.biz_type = biz_type        # type: str
        self.biz_id = biz_id            # type: str
        self.name = name                # type: str
        self.id_card_number = id_card_number  # type: str
        self.id_card_front_image_url = id_card_front_image_url  # type: str
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.id_card_number, 'id_card_number')

    def to_map(self):
        result = {}
        result['IdCardBackImageUrl'] = self.id_card_back_image_url
        result['FaceImageUrl'] = self.face_image_url
        result['BizType'] = self.biz_type
        result['BizId'] = self.biz_id
        result['Name'] = self.name
        result['IdCardNumber'] = self.id_card_number
        result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.id_card_back_image_url = map.get('IdCardBackImageUrl')
        self.face_image_url = map.get('FaceImageUrl')
        self.biz_type = map.get('BizType')
        self.biz_id = map.get('BizId')
        self.name = map.get('Name')
        self.id_card_number = map.get('IdCardNumber')
        self.id_card_front_image_url = map.get('IdCardFrontImageUrl')
        self.user_id = map.get('UserId')
        return self


class VerifyMaterialResponse(TeaModel):
    def __init__(self, request_id=None, verify_token=None, verify_status=None, authority_comparision_score=None,
                 id_card_face_comparison_score=None, material=None):
        self.request_id = request_id    # type: str
        self.verify_token = verify_token  # type: str
        self.verify_status = verify_status  # type: int
        self.authority_comparision_score = authority_comparision_score  # type: float
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.material = material        # type: VerifyMaterialResponseMaterial

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_token, 'verify_token')
        self.validate_required(self.verify_status, 'verify_status')
        self.validate_required(self.authority_comparision_score, 'authority_comparision_score')
        self.validate_required(self.id_card_face_comparison_score, 'id_card_face_comparison_score')
        self.validate_required(self.material, 'material')
        if self.material:
            self.material.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VerifyToken'] = self.verify_token
        result['VerifyStatus'] = self.verify_status
        result['AuthorityComparisionScore'] = self.authority_comparision_score
        result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        else:
            result['Material'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.verify_token = map.get('VerifyToken')
        self.verify_status = map.get('VerifyStatus')
        self.authority_comparision_score = map.get('AuthorityComparisionScore')
        self.id_card_face_comparison_score = map.get('IdCardFaceComparisonScore')
        if map.get('Material') is not None:
            temp_model = VerifyMaterialResponseMaterial()
            self.material = temp_model.from_map(map['Material'])
        else:
            self.material = None
        return self


class VerifyMaterialResponseMaterialIdCardInfo(TeaModel):
    def __init__(self, number=None, address=None, nationality=None, end_date=None, front_image_url=None,
                 authority=None, sex=None, name=None, birth=None, back_image_url=None, start_date=None):
        self.number = number            # type: str
        self.address = address          # type: str
        self.nationality = nationality  # type: str
        self.end_date = end_date        # type: str
        self.front_image_url = front_image_url  # type: str
        self.authority = authority      # type: str
        self.sex = sex                  # type: str
        self.name = name                # type: str
        self.birth = birth              # type: str
        self.back_image_url = back_image_url  # type: str
        self.start_date = start_date    # type: str

    def validate(self):
        self.validate_required(self.number, 'number')
        self.validate_required(self.address, 'address')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.front_image_url, 'front_image_url')
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.sex, 'sex')
        self.validate_required(self.name, 'name')
        self.validate_required(self.birth, 'birth')
        self.validate_required(self.back_image_url, 'back_image_url')
        self.validate_required(self.start_date, 'start_date')

    def to_map(self):
        result = {}
        result['Number'] = self.number
        result['Address'] = self.address
        result['Nationality'] = self.nationality
        result['EndDate'] = self.end_date
        result['FrontImageUrl'] = self.front_image_url
        result['Authority'] = self.authority
        result['Sex'] = self.sex
        result['Name'] = self.name
        result['Birth'] = self.birth
        result['BackImageUrl'] = self.back_image_url
        result['StartDate'] = self.start_date
        return result

    def from_map(self, map={}):
        self.number = map.get('Number')
        self.address = map.get('Address')
        self.nationality = map.get('Nationality')
        self.end_date = map.get('EndDate')
        self.front_image_url = map.get('FrontImageUrl')
        self.authority = map.get('Authority')
        self.sex = map.get('Sex')
        self.name = map.get('Name')
        self.birth = map.get('Birth')
        self.back_image_url = map.get('BackImageUrl')
        self.start_date = map.get('StartDate')
        return self


class VerifyMaterialResponseMaterial(TeaModel):
    def __init__(self, face_image_url=None, id_card_name=None, id_card_number=None, face_quality=None,
                 face_global_url=None, face_mask=None, id_card_info=None):
        self.face_image_url = face_image_url  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.face_quality = face_quality  # type: str
        self.face_global_url = face_global_url  # type: str
        self.face_mask = face_mask      # type: str
        self.id_card_info = id_card_info  # type: VerifyMaterialResponseMaterialIdCardInfo

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.id_card_name, 'id_card_name')
        self.validate_required(self.id_card_number, 'id_card_number')
        self.validate_required(self.face_quality, 'face_quality')
        self.validate_required(self.face_global_url, 'face_global_url')
        self.validate_required(self.face_mask, 'face_mask')
        self.validate_required(self.id_card_info, 'id_card_info')
        if self.id_card_info:
            self.id_card_info.validate()

    def to_map(self):
        result = {}
        result['FaceImageUrl'] = self.face_image_url
        result['IdCardName'] = self.id_card_name
        result['IdCardNumber'] = self.id_card_number
        result['FaceQuality'] = self.face_quality
        result['FaceGlobalUrl'] = self.face_global_url
        result['FaceMask'] = self.face_mask
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        else:
            result['IdCardInfo'] = None
        return result

    def from_map(self, map={}):
        self.face_image_url = map.get('FaceImageUrl')
        self.id_card_name = map.get('IdCardName')
        self.id_card_number = map.get('IdCardNumber')
        self.face_quality = map.get('FaceQuality')
        self.face_global_url = map.get('FaceGlobalUrl')
        self.face_mask = map.get('FaceMask')
        if map.get('IdCardInfo') is not None:
            temp_model = VerifyMaterialResponseMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(map['IdCardInfo'])
        else:
            self.id_card_info = None
        return self


class DescribeVerifyResultRequest(TeaModel):
    def __init__(self, biz_id=None, biz_type=None):
        self.biz_id = biz_id            # type: str
        self.biz_type = biz_type        # type: str

    def validate(self):
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.biz_type, 'biz_type')

    def to_map(self):
        result = {}
        result['BizId'] = self.biz_id
        result['BizType'] = self.biz_type
        return result

    def from_map(self, map={}):
        self.biz_id = map.get('BizId')
        self.biz_type = map.get('BizType')
        return self


class DescribeVerifyResultResponse(TeaModel):
    def __init__(self, request_id=None, verify_status=None, authority_comparision_score=None,
                 face_comparison_score=None, id_card_face_comparison_score=None, material=None):
        self.request_id = request_id    # type: str
        self.verify_status = verify_status  # type: int
        self.authority_comparision_score = authority_comparision_score  # type: float
        self.face_comparison_score = face_comparison_score  # type: float
        self.id_card_face_comparison_score = id_card_face_comparison_score  # type: float
        self.material = material        # type: DescribeVerifyResultResponseMaterial

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_status, 'verify_status')
        self.validate_required(self.authority_comparision_score, 'authority_comparision_score')
        self.validate_required(self.face_comparison_score, 'face_comparison_score')
        self.validate_required(self.id_card_face_comparison_score, 'id_card_face_comparison_score')
        self.validate_required(self.material, 'material')
        if self.material:
            self.material.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VerifyStatus'] = self.verify_status
        result['AuthorityComparisionScore'] = self.authority_comparision_score
        result['FaceComparisonScore'] = self.face_comparison_score
        result['IdCardFaceComparisonScore'] = self.id_card_face_comparison_score
        if self.material is not None:
            result['Material'] = self.material.to_map()
        else:
            result['Material'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.verify_status = map.get('VerifyStatus')
        self.authority_comparision_score = map.get('AuthorityComparisionScore')
        self.face_comparison_score = map.get('FaceComparisonScore')
        self.id_card_face_comparison_score = map.get('IdCardFaceComparisonScore')
        if map.get('Material') is not None:
            temp_model = DescribeVerifyResultResponseMaterial()
            self.material = temp_model.from_map(map['Material'])
        else:
            self.material = None
        return self


class DescribeVerifyResultResponseMaterialIdCardInfo(TeaModel):
    def __init__(self, number=None, address=None, nationality=None, end_date=None, front_image_url=None,
                 authority=None, sex=None, name=None, birth=None, back_image_url=None, start_date=None):
        self.number = number            # type: str
        self.address = address          # type: str
        self.nationality = nationality  # type: str
        self.end_date = end_date        # type: str
        self.front_image_url = front_image_url  # type: str
        self.authority = authority      # type: str
        self.sex = sex                  # type: str
        self.name = name                # type: str
        self.birth = birth              # type: str
        self.back_image_url = back_image_url  # type: str
        self.start_date = start_date    # type: str

    def validate(self):
        self.validate_required(self.number, 'number')
        self.validate_required(self.address, 'address')
        self.validate_required(self.nationality, 'nationality')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.front_image_url, 'front_image_url')
        self.validate_required(self.authority, 'authority')
        self.validate_required(self.sex, 'sex')
        self.validate_required(self.name, 'name')
        self.validate_required(self.birth, 'birth')
        self.validate_required(self.back_image_url, 'back_image_url')
        self.validate_required(self.start_date, 'start_date')

    def to_map(self):
        result = {}
        result['Number'] = self.number
        result['Address'] = self.address
        result['Nationality'] = self.nationality
        result['EndDate'] = self.end_date
        result['FrontImageUrl'] = self.front_image_url
        result['Authority'] = self.authority
        result['Sex'] = self.sex
        result['Name'] = self.name
        result['Birth'] = self.birth
        result['BackImageUrl'] = self.back_image_url
        result['StartDate'] = self.start_date
        return result

    def from_map(self, map={}):
        self.number = map.get('Number')
        self.address = map.get('Address')
        self.nationality = map.get('Nationality')
        self.end_date = map.get('EndDate')
        self.front_image_url = map.get('FrontImageUrl')
        self.authority = map.get('Authority')
        self.sex = map.get('Sex')
        self.name = map.get('Name')
        self.birth = map.get('Birth')
        self.back_image_url = map.get('BackImageUrl')
        self.start_date = map.get('StartDate')
        return self


class DescribeVerifyResultResponseMaterial(TeaModel):
    def __init__(self, face_image_url=None, id_card_name=None, id_card_number=None, face_quality=None,
                 face_global_url=None, face_mask=None, id_card_info=None, video_urls=None):
        self.face_image_url = face_image_url  # type: str
        self.id_card_name = id_card_name  # type: str
        self.id_card_number = id_card_number  # type: str
        self.face_quality = face_quality  # type: str
        self.face_global_url = face_global_url  # type: str
        self.face_mask = face_mask      # type: bool
        self.id_card_info = id_card_info  # type: DescribeVerifyResultResponseMaterialIdCardInfo
        self.video_urls = video_urls    # type: List[str]

    def validate(self):
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.id_card_name, 'id_card_name')
        self.validate_required(self.id_card_number, 'id_card_number')
        self.validate_required(self.face_quality, 'face_quality')
        self.validate_required(self.face_global_url, 'face_global_url')
        self.validate_required(self.face_mask, 'face_mask')
        self.validate_required(self.id_card_info, 'id_card_info')
        if self.id_card_info:
            self.id_card_info.validate()
        self.validate_required(self.video_urls, 'video_urls')

    def to_map(self):
        result = {}
        result['FaceImageUrl'] = self.face_image_url
        result['IdCardName'] = self.id_card_name
        result['IdCardNumber'] = self.id_card_number
        result['FaceQuality'] = self.face_quality
        result['FaceGlobalUrl'] = self.face_global_url
        result['FaceMask'] = self.face_mask
        if self.id_card_info is not None:
            result['IdCardInfo'] = self.id_card_info.to_map()
        else:
            result['IdCardInfo'] = None
        result['VideoUrls'] = self.video_urls
        return result

    def from_map(self, map={}):
        self.face_image_url = map.get('FaceImageUrl')
        self.id_card_name = map.get('IdCardName')
        self.id_card_number = map.get('IdCardNumber')
        self.face_quality = map.get('FaceQuality')
        self.face_global_url = map.get('FaceGlobalUrl')
        self.face_mask = map.get('FaceMask')
        if map.get('IdCardInfo') is not None:
            temp_model = DescribeVerifyResultResponseMaterialIdCardInfo()
            self.id_card_info = temp_model.from_map(map['IdCardInfo'])
        else:
            self.id_card_info = None
        self.video_urls = map.get('VideoUrls')
        return self


class DescribeOssUploadTokenRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeOssUploadTokenResponse(TeaModel):
    def __init__(self, request_id=None, oss_upload_token=None):
        self.request_id = request_id    # type: str
        self.oss_upload_token = oss_upload_token  # type: DescribeOssUploadTokenResponseOssUploadToken

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.oss_upload_token, 'oss_upload_token')
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        else:
            result['OssUploadToken'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('OssUploadToken') is not None:
            temp_model = DescribeOssUploadTokenResponseOssUploadToken()
            self.oss_upload_token = temp_model.from_map(map['OssUploadToken'])
        else:
            self.oss_upload_token = None
        return self


class DescribeOssUploadTokenResponseOssUploadToken(TeaModel):
    def __init__(self, bucket=None, end_point=None, path=None, expired=None, secret=None, key=None, token=None):
        self.bucket = bucket            # type: str
        self.end_point = end_point      # type: str
        self.path = path                # type: str
        self.expired = expired          # type: int
        self.secret = secret            # type: str
        self.key = key                  # type: str
        self.token = token              # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.end_point, 'end_point')
        self.validate_required(self.path, 'path')
        self.validate_required(self.expired, 'expired')
        self.validate_required(self.secret, 'secret')
        self.validate_required(self.key, 'key')
        self.validate_required(self.token, 'token')

    def to_map(self):
        result = {}
        result['Bucket'] = self.bucket
        result['EndPoint'] = self.end_point
        result['Path'] = self.path
        result['Expired'] = self.expired
        result['Secret'] = self.secret
        result['Key'] = self.key
        result['Token'] = self.token
        return result

    def from_map(self, map={}):
        self.bucket = map.get('Bucket')
        self.end_point = map.get('EndPoint')
        self.path = map.get('Path')
        self.expired = map.get('Expired')
        self.secret = map.get('Secret')
        self.key = map.get('Key')
        self.token = map.get('Token')
        return self


class DescribeVerifyTokenRequest(TeaModel):
    def __init__(self, id_card_back_image_url=None, biz_type=None, failed_redirect_url=None,
                 face_retained_image_url=None, callback_seed=None, id_card_front_image_url=None, user_id=None, biz_id=None, name=None,
                 id_card_number=None, passed_redirect_url=None, callback_url=None, user_ip=None, user_phone_number=None,
                 user_regist_time=None):
        self.id_card_back_image_url = id_card_back_image_url  # type: str
        self.biz_type = biz_type        # type: str
        self.failed_redirect_url = failed_redirect_url  # type: str
        self.face_retained_image_url = face_retained_image_url  # type: str
        self.callback_seed = callback_seed  # type: str
        self.id_card_front_image_url = id_card_front_image_url  # type: str
        self.user_id = user_id          # type: str
        self.biz_id = biz_id            # type: str
        self.name = name                # type: str
        self.id_card_number = id_card_number  # type: str
        self.passed_redirect_url = passed_redirect_url  # type: str
        self.callback_url = callback_url  # type: str
        self.user_ip = user_ip          # type: str
        self.user_phone_number = user_phone_number  # type: str
        self.user_regist_time = user_regist_time  # type: int

    def validate(self):
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.biz_id, 'biz_id')

    def to_map(self):
        result = {}
        result['IdCardBackImageUrl'] = self.id_card_back_image_url
        result['BizType'] = self.biz_type
        result['FailedRedirectUrl'] = self.failed_redirect_url
        result['FaceRetainedImageUrl'] = self.face_retained_image_url
        result['CallbackSeed'] = self.callback_seed
        result['IdCardFrontImageUrl'] = self.id_card_front_image_url
        result['UserId'] = self.user_id
        result['BizId'] = self.biz_id
        result['Name'] = self.name
        result['IdCardNumber'] = self.id_card_number
        result['PassedRedirectUrl'] = self.passed_redirect_url
        result['CallbackUrl'] = self.callback_url
        result['UserIp'] = self.user_ip
        result['UserPhoneNumber'] = self.user_phone_number
        result['UserRegistTime'] = self.user_regist_time
        return result

    def from_map(self, map={}):
        self.id_card_back_image_url = map.get('IdCardBackImageUrl')
        self.biz_type = map.get('BizType')
        self.failed_redirect_url = map.get('FailedRedirectUrl')
        self.face_retained_image_url = map.get('FaceRetainedImageUrl')
        self.callback_seed = map.get('CallbackSeed')
        self.id_card_front_image_url = map.get('IdCardFrontImageUrl')
        self.user_id = map.get('UserId')
        self.biz_id = map.get('BizId')
        self.name = map.get('Name')
        self.id_card_number = map.get('IdCardNumber')
        self.passed_redirect_url = map.get('PassedRedirectUrl')
        self.callback_url = map.get('CallbackUrl')
        self.user_ip = map.get('UserIp')
        self.user_phone_number = map.get('UserPhoneNumber')
        self.user_regist_time = map.get('UserRegistTime')
        return self


class DescribeVerifyTokenResponse(TeaModel):
    def __init__(self, request_id=None, verify_page_url=None, verify_token=None, oss_upload_token=None):
        self.request_id = request_id    # type: str
        self.verify_page_url = verify_page_url  # type: str
        self.verify_token = verify_token  # type: str
        self.oss_upload_token = oss_upload_token  # type: DescribeVerifyTokenResponseOssUploadToken

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.verify_page_url, 'verify_page_url')
        self.validate_required(self.verify_token, 'verify_token')
        self.validate_required(self.oss_upload_token, 'oss_upload_token')
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VerifyPageUrl'] = self.verify_page_url
        result['VerifyToken'] = self.verify_token
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()
        else:
            result['OssUploadToken'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.verify_page_url = map.get('VerifyPageUrl')
        self.verify_token = map.get('VerifyToken')
        if map.get('OssUploadToken') is not None:
            temp_model = DescribeVerifyTokenResponseOssUploadToken()
            self.oss_upload_token = temp_model.from_map(map['OssUploadToken'])
        else:
            self.oss_upload_token = None
        return self


class DescribeVerifyTokenResponseOssUploadToken(TeaModel):
    def __init__(self, bucket=None, end_point=None, path=None, expired=None, secret=None, key=None, token=None):
        self.bucket = bucket            # type: str
        self.end_point = end_point      # type: str
        self.path = path                # type: str
        self.expired = expired          # type: int
        self.secret = secret            # type: str
        self.key = key                  # type: str
        self.token = token              # type: str

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.end_point, 'end_point')
        self.validate_required(self.path, 'path')
        self.validate_required(self.expired, 'expired')
        self.validate_required(self.secret, 'secret')
        self.validate_required(self.key, 'key')
        self.validate_required(self.token, 'token')

    def to_map(self):
        result = {}
        result['Bucket'] = self.bucket
        result['EndPoint'] = self.end_point
        result['Path'] = self.path
        result['Expired'] = self.expired
        result['Secret'] = self.secret
        result['Key'] = self.key
        result['Token'] = self.token
        return result

    def from_map(self, map={}):
        self.bucket = map.get('Bucket')
        self.end_point = map.get('EndPoint')
        self.path = map.get('Path')
        self.expired = map.get('Expired')
        self.secret = map.get('Secret')
        self.key = map.get('Key')
        self.token = map.get('Token')
        return self


