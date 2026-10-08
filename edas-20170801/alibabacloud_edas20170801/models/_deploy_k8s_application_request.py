# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployK8sApplicationRequest(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        app_id: str = None,
        args: str = None,
        batch_timeout: int = None,
        batch_wait_time: int = None,
        build_pack_id: str = None,
        canary_rule_id: str = None,
        change_order_desc: str = None,
        command: str = None,
        config_mount_descs: str = None,
        cpu_limit: int = None,
        cpu_request: int = None,
        custom_affinity: str = None,
        custom_agent_version: str = None,
        custom_tolerations: str = None,
        deploy_across_nodes: str = None,
        deploy_across_zones: str = None,
        edas_container_version: str = None,
        empty_dirs: str = None,
        enable_ahas: bool = None,
        enable_empty_push_reject: bool = None,
        enable_lossless_rule: bool = None,
        env_froms: str = None,
        envs: str = None,
        image: str = None,
        image_platforms: str = None,
        image_tag: str = None,
        init_containers: str = None,
        jdk: str = None,
        java_start_up_config: str = None,
        labels: str = None,
        limit_ephemeral_storage: int = None,
        liveness: str = None,
        local_volume: str = None,
        lossless_rule_aligned: bool = None,
        lossless_rule_delay_time: int = None,
        lossless_rule_func_type: int = None,
        lossless_rule_related: bool = None,
        lossless_rule_warmup_time: int = None,
        mcpu_limit: int = None,
        mcpu_request: int = None,
        memory_limit: int = None,
        memory_request: int = None,
        mount_descs: str = None,
        nas_id: str = None,
        package_url: str = None,
        package_version: str = None,
        package_version_id: str = None,
        post_start: str = None,
        pre_stop: str = None,
        pvc_mount_descs: str = None,
        readiness: str = None,
        replicas: int = None,
        requests_ephemeral_storage: int = None,
        runtime_class_name: str = None,
        security_context: str = None,
        sidecars: str = None,
        sls_configs: str = None,
        startup: str = None,
        storage_type: str = None,
        terminate_grace_period: int = None,
        traffic_control_strategy: str = None,
        update_strategy: str = None,
        uri_encoding: str = None,
        use_body_encoding: bool = None,
        user_base_image_url: str = None,
        volumes_str: str = None,
        web_container: str = None,
        web_container_config: str = None,
    ):
        # The annotations for the application pod.
        self.annotations = annotations
        # The application ID. Obtain the ID by calling the ListApplication operation. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The arguments for the container startup command. The value must be a JSON array of strings, such as `["Argument 1", "Argument 2"]`. To clear the arguments, set the parameter to an empty JSON array `"[]"`.
        self.args = args
        # The timeout period for a single batch release. Unit: seconds.
        self.batch_timeout = batch_timeout
        # The minimum interval for a phased release of pods. For more information, see [minReadySeconds](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#min-ready-seconds).
        self.batch_wait_time = batch_wait_time
        # The build package number for EDAS Container:
        # 
        # - If you do not need to change the EDAS Container version during deployment, you can leave this parameter unset.
        # 
        # - To update the EDAS Container version of the target application during this deployment, you must set this parameter.
        # 
        # You can obtain the number in two ways:
        # 
        # - Call the ListBuildPack operation to query the list of container versions. For more information, see [ListBuildPack](https://help.aliyun.com/document_detail/423222.html).
        # 
        # - Obtain it from the **Build Package Number** column in the [Version guide](https://help.aliyun.com/document_detail/92614.html) table. For example, `59` indicates `EDAS Container 3.5.8`.
        self.build_pack_id = build_pack_id
        # The ID of the canary release rule policy.
        self.canary_rule_id = canary_rule_id
        # The description of the change record.
        self.change_order_desc = change_order_desc
        # The container startup command.
        # 
        # > To clear this configuration, set the parameter to an empty string `""`.
        self.command = command
        # Configures Kubernetes ConfigMap and Secret mounts. This lets you mount a ConfigMap or Secret to a specified container directory. The parameters for \\`ConfigMountDescs\\` are as follows:
        # 
        # - \\`name\\`: The name of the ConfigMap or Secret.
        # 
        # - \\`type\\`: The configuration type. \\`ConfigMap\\` and \\`Secret\\` are supported.
        # 
        # - \\`mountPath\\`: The mount path. An absolute path in the container that starts with a forward slash (/).
        self.config_mount_descs = config_mount_descs
        # The CPU limit for the application instance during runtime. Unit: cores. A value of 0 means no limit.
        self.cpu_limit = cpu_limit
        # The CPU quota to request for the application instance during runtime. Setting this parameter is recommended.
        # Unit: cores. A value of 0 means no limit.
        # 
        # > If you set this parameter, also set the CpuLimit parameter. The value of CpuRequest must be less than or equal to the value of CpuLimit.
        self.cpu_request = cpu_request
        # The pod affinity configuration. This takes effect only when both \\`DeployAcrossNodes\\` and \\`DeployAcrossZones\\` are \\`false\\`.
        self.custom_affinity = custom_affinity
        # Sets the version of the custom Application Real-Time Monitoring Service (ARMS) agent to mount to the application.
        # 
        # > This feature is available only to whitelisted users. To use this feature, submit a ticket to be added to the whitelist.
        self.custom_agent_version = custom_agent_version
        # The pod scheduling toleration configuration. This takes effect only when both \\`DeployAcrossNodes\\` and \\`DeployAcrossZones\\` are \\`false\\`.
        self.custom_tolerations = custom_tolerations
        # Specifies whether to distribute application instances across multiple nodes. \\`true\\` indicates yes, and other values indicate no.
        self.deploy_across_nodes = deploy_across_nodes
        # Specifies whether to distribute application instances across multiple zones. \\`true\\` indicates yes, and other values indicate no.
        self.deploy_across_zones = deploy_across_zones
        # The EDAS Container version on which the deployment package depends. This parameter applies to HSF applications deployed using WAR packages. It is not supported for image-based deployments.
        self.edas_container_version = edas_container_version
        # Configures Kubernetes \\`emptyDir\\` mounts. This lets you mount an \\`emptyDir\\` volume to a specified container directory. The parameters for \\`EmptyDirs\\` are as follows:
        # 
        # - \\`mountPath\\`: The container mount path. This is required.
        # 
        # - \\`readOnly\\`: Specifies whether the volume is read-only. Optional. \\`true\\` for read-only, \\`false\\` for read-write. The default is \\`false\\`.
        # 
        # - \\`subPathExpr\\`: The subdirectory expression. Optional.
        self.empty_dirs = empty_dirs
        # Specifies whether to connect to Application High Availability Service (AHAS).
        self.enable_ahas = enable_ahas
        # Specifies whether to enable empty push protection:
        # 
        # - \\`true\\`: Enable empty push protection.
        # 
        # - \\`false\\`: Do not enable empty push protection.
        self.enable_empty_push_reject = enable_empty_push_reject
        # Specifies whether to enable the graceful start rule:
        # 
        # - \\`true\\`: Enable the graceful start rule.
        # 
        # - \\`false\\`: Do not enable the graceful start rule.
        self.enable_lossless_rule = enable_lossless_rule
        # Configures environment variables of the Kubernetes \\`EnvFrom\\` type. This mounts a specified ConfigMap or Secret to a directory. Each key corresponds to a file in the directory, and the file content is the value of the key.
        # 
        # The parameters for \\`EnvFroms\\` are as follows.
        # 
        # - \\`configMapRef\\`: A reference to a ConfigMap. This field includes the following parameter:
        # 
        #   - \\`name\\`: The name of the ConfigMap.
        # 
        # - \\`secretRef\\`: A reference to a Secret. This field includes the following parameter:
        # 
        #   - \\`name\\`: The name of the Secret.
        self.env_froms = env_froms
        # The environment variables for the deployment. The value must be a JSON array of objects. Three types of environment variables are supported: regular, Kubernetes ConfigMap, and Kubernetes Secret. The format for a regular environment variable is as follows:
        # 
        # `{"name":"x", "value": "y"}`
        # 
        # A ConfigMap environment variable injects the value of a specified key from a ConfigMap into the container\\"s environment variables. The format is as follows:
        # 
        # `{ "name": "x2", "valueFrom": { "configMapKeyRef": { "name": "my-config", "key": "y2" } } }`
        # 
        # A Secret environment variable injects the value of a specified key from a Secret into the container\\"s environment variables. The format is as follows:
        # 
        # `{ "name": "x3", "valueFrom": { "secretKeyRef": { "name": "my-secret", "key": "y3" } } }`
        # 
        # > To clear this configuration, set the parameter to an empty JSON array \\`[]\\`.
        self.envs = envs
        # The full URL of the image. This parameter overwrites the ImageTag parameter.
        self.image = image
        # The target platform architecture for the image. This is valid when deploying with a WAR or JAR file. Examples:
        # 
        # - To specify the x86-64 architecture: \\`linux/amd64\\`
        # 
        # - To specify the ARM 64 architecture: \\`linux/arm64\\`
        # 
        # - To build a dual-architecture image: \\`linux/amd64,linux/arm64\\`
        # 
        # - If you do not enter a value, the default architecture is used.
        self.image_platforms = image_platforms
        # The image tag.
        self.image_tag = image_tag
        # Sets an init container for the application pod. The container configuration is in YAML format. The value is the base64-encoded YAML configuration of the init container.
        self.init_containers = init_containers
        # The JDK version on which the deployment package depends. Valid values: Open JDK 7, Open JDK 8, or Custom OpenJDK. This parameter is not supported for image-based deployments. If you use Custom OpenJDK, you must also configure the \\`UserBaseImageUrl\\` field.
        self.jdk = jdk
        # The Java startup parameters. You can configure memory, application, garbage collection (GC) policy, tools, service registration and discovery, and custom settings. Correctly configuring these parameters helps reduce GC overhead, shorten server response time, and improve throughput. The parameter is a JSON string. \\`original\\` is the configuration value, and \\`startup\\` is the startup parameter. The system automatically concatenates all \\`startup\\` values as the Java startup parameters for the application. Set to `""` or `"{}"` to delete the configuration.
        self.java_start_up_config = java_start_up_config
        # The labels for the application pod.
        self.labels = labels
        # The upper limit of the temporary storage resource requirement. Unit: GB. A value of 0 means no limit.
        self.limit_ephemeral_storage = limit_ephemeral_storage
        # The liveness probe for the container. Example: `{"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"tcpSocket":{"host":"", "port":8080}}`. To delete this configuration, set the parameter to `""` or `{}`. If you do not set this parameter, the configuration is ignored.
        self.liveness = liveness
        # The configuration for mounting a host file to a container. Example: `[{"type":"","nodePath":"/localfiles","mountPath":"/app/files"},{"type":"Directory","nodePath":"/mnt","mountPath":"/app/storage"}]`. In this example, \\`nodePath\\` is the host path, \\`mountPath\\` is the path in the container, and \\`type\\` is the mount type.
        self.local_volume = local_volume
        # Specifies whether to enable the graceful rolling deployment mode to complete service registration before the readiness probe succeeds:
        # 
        # - \\`true\\`: This switch provides a health check for the application on port 55199 and the \\`/health\\` path without intrusion. When service registration is complete, the interface returns 200. Otherwise, it returns 500.
        # 
        # > If \\`LosslessRuleRelated\\` is also set to \\`true\\`, this interface checks whether service prefetch is complete.
        # 
        # - \\`false\\`: Does not provide an interface for the application to check if service registration is complete.
        self.lossless_rule_aligned = lossless_rule_aligned
        # The service registration latency. Unit: seconds. The value ranges from 0 to 86400.
        self.lossless_rule_delay_time = lossless_rule_delay_time
        # The service prefetch curve. The value ranges from 0 to 20. The default is 2, which is suitable for general prefetch scenarios. This indicates that the traffic receiving curve of the service provider follows a quadratic curve during the prefetch period.
        self.lossless_rule_func_type = lossless_rule_func_type
        # Specifies whether to enable the graceful rolling deployment mode to complete service prefetch before the readiness probe succeeds:
        # 
        # - \\`true\\`: This switch provides a health check for the application on port 55199 and the \\`/health\\` path without intrusion. When service prefetch is complete, the interface returns 200. Otherwise, it returns 500.
        # 
        # - \\`false\\`: Does not provide an interface for the application to check if service prefetch is complete.
        self.lossless_rule_related = lossless_rule_related
        # The service prefetch duration. Unit: seconds. The value ranges from 0 to 86400.
        self.lossless_rule_warmup_time = lossless_rule_warmup_time
        # The maximum CPU that can be used. Unit: cores. A value of 0 means no limit.
        self.mcpu_limit = mcpu_limit
        # The minimum CPU resource requirement. Unit: cores. A value of 0 means no limit.
        # 
        # > If you set this parameter, you must also set the \\`CpuLimit\\` parameter. The value must be less than or equal to the value of \\`CpuLimit\\`.
        self.mcpu_request = mcpu_request
        # The memory limit for the application instance during runtime. Unit: MB. A value of 0 means no limit.
        self.memory_limit = memory_limit
        # The memory quota to request for the application instance during runtime. Setting this parameter is recommended. Unit: MB. A value of 0 means no request.
        # 
        # > If you set this parameter, also set the MemoryLimit parameter. The value of MemoryRequest must be less than or equal to the value of MemoryLimit.
        self.memory_request = memory_request
        # The mount configurations, which are a serialized JSON string. Example: `[{"nasPath": "/k8s","mountPath": "/mnt"},{"nasPath": "/files","mountPath": "/app/files"}]`. In this example, \\`nasPath\\` is the file storage path and \\`mountPath\\` is the path in the container to which the file system is mounted.
        self.mount_descs = mount_descs
        # The ID of the Apsara File Storage NAS (NAS) file system to mount. The NAS file system must be in the same region as the cluster. It must have an available mount target quota, or its mount target must be on a vSwitch in the VPC. If you do not set this parameter but the \\`mountDescs\\` field exists, a NAS file system is automatically purchased and mounted to a vSwitch in the VPC by default.
        self.nas_id = nas_id
        # The URL of the deployment package. Configure this parameter for applications deployed using a FatJar or WAR package.
        # 
        # > The Java or Python SDK for EDAS POP API must be version 2.44.0 or later.
        self.package_url = package_url
        # The version number of the deployment package. This parameter is required for WAR and FatJar packages. You can define the meaning of the version number.
        # 
        # > The Java or Python SDK for EDAS POP API must be version 2.44.0 or later.
        self.package_version = package_version
        # The ID of the deployment package version.
        self.package_version_id = package_version_id
        # The script to execute after the container starts. Example: `{"exec":{"command":["cat","/etc/group"]}}`. To delete this configuration, set the parameter to `{}`. If you do not set this parameter, the configuration is ignored.
        self.post_start = post_start
        # The script to execute before stopping the container. Example: `{"tcpSocket":{"host":"", "port":8080}}`.
        # To delete this configuration, set the parameter to `{}`. If you do not set this parameter, the configuration is ignored.
        self.pre_stop = pre_stop
        # Configures Kubernetes PersistentVolumeClaim (PVC) mounts. This lets you mount a Kubernetes PVC volume to a specified container directory. The parameters for \\`PvcMountDescs\\` are as follows:
        # 
        # - \\`pvcName\\`: The name of the PVC volume. The PVC volume must already exist and be in the Bound state.
        # 
        # - \\`mountPaths\\`: A list of mount directories. You can configure multiple mount directories. Each mount directory supports the following two parameters:
        # 
        #   - \\`mountPath\\`: The mount path. An absolute path in the container that starts with a forward slash (/).
        # 
        #   - \\`readOnly\\`: The mount mode. \\`true\\` for read-only, \\`false\\` for read-write. The default is \\`false\\`.
        self.pvc_mount_descs = pvc_mount_descs
        # The readiness probe for the container. If the probe fails, traffic from the Kubernetes service is not routed to the container. Example: `{"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"httpGet": {"path": "/consumer","port": 8080,"scheme": "HTTP","httpHeaders": [{"name": "test","value": "testvalue"}]}}`. To delete this configuration, set the parameter to `""` or `{}`. If you do not set this parameter, the configuration is ignored.
        self.readiness = readiness
        # The number of application instances. The minimum value is 0.
        self.replicas = replicas
        # The minimum temporary storage resource requirement. Unit: GB. A value of 0 means no limit.
        self.requests_ephemeral_storage = requests_ephemeral_storage
        # The container runtime type:
        # 
        # - \\`runc\\`: regular container runtime.
        # 
        # - \\`runv\\`: sandboxed container.
        # 
        # This parameter applies only to clusters that use sandboxed containers.
        self.runtime_class_name = runtime_class_name
        # Sets the \\`SecurityContext\\` property for the application pod container. The value is the base64-encoded YAML configuration of the \\`SecurityContext\\`.
        self.security_context = security_context
        # Sets a sidecar container for the application pod. The container configuration is in YAML format. The value is the base64-encoded YAML configuration of the sidecar container.
        self.sidecars = sidecars
        # The Logstore configuration. Set to `""` or `"{}"` to delete the configuration:
        # 
        # - \\`Configs\\`:
        # 
        #   - \\`type\\`: The collection type. \\`file\\` for file type, \\`stdout\\` for standard output type.
        # 
        #   - \\`Logstore\\`: The name of the Logstore. Make sure the Logstore name is unique within the same cluster. The name must follow these rules:
        # 
        #     - It can only contain lowercase letters, numbers, hyphens (-), and underscores (_).
        # 
        #     - It must start and end with a lowercase letter or a number.
        # 
        #     - The name must be 3 to 63 characters long. If left empty, the system generates a name automatically.
        # 
        #   - \\`LogDir\\`: If the type is standard output, the collection path is \\`stdout.log\\`. If the type is file, this is the path of the file to collect. Wildcards are supported. The collection path must match the regular expression: `^/(.+)/(.*)^/$`.
        self.sls_configs = sls_configs
        # The startup probe can be used to perform liveness checks on slow-starting containers to prevent them from being killed before they are up and running. Example: {"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"httpGet": {"path": "/consumer","port": 8080,"scheme": "HTTP","httpHeaders": [{"name": "test","value": "testvalue"}]}}.
        # 
        # To delete this configuration, set the parameter to "" or {}. If you do not set this parameter, the configuration is ignored.
        self.startup = startup
        # The storage type of the NAS file system. Valid values:
        # 
        # - General-purpose NAS: \\`Capacity\\` and \\`Performance\\`
        # 
        # - Extreme NAS: \\`standard\\` and \\`advance\\`
        # 
        # Currently, only the \\`Performance\\` type is supported.
        self.storage_type = storage_type
        # The graceful stop timeout period for the application. Unit: seconds.
        self.terminate_grace_period = terminate_grace_period
        # The traffic control policy for phased release.
        self.traffic_control_strategy = traffic_control_strategy
        # The phased release policy.
        # 
        # - Example 1: Phased release with one canary instance, followed by two batches, automatic batching, and a 1-minute interval.
        #   `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":1},"grayUpdate":{"gray":1}}`
        # 
        # - Example 2: Phased release with one canary instance, followed by two batches and manual batching.
        #   `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"manual"},"grayUpdate":{"gray":1}}`
        # 
        # - Example 3: Phased release in two batches, with automatic batching and a 0-minute interval.
        #   `{"type":"BatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":0}}`
        self.update_strategy = update_strategy
        # The URI encoding format. Supported formats: ISO-8859-1, GBK, GB2312, and UTF-8.
        # 
        # > If you do not set this parameter in the application configuration, the default Tomcat value is used.
        self.uri_encoding = uri_encoding
        # Specifies whether to enable \\`useBodyEncodingForURI\\`.
        # 
        # > If you do not set this parameter in the application configuration, the default value \\`false\\` is used.
        self.use_body_encoding = use_body_encoding
        # When using a custom JDK runtime, you must configure the base image address. This address must be publicly accessible. The EDAS server pulls this image to build the application image.
        self.user_base_image_url = user_base_image_url
        # The data volumes.
        self.volumes_str = volumes_str
        # The Tomcat version on which the deployment package depends. This parameter applies to Spring Cloud and Dubbo applications deployed using WAR packages. It is not supported for image-based deployments.
        self.web_container = web_container
        # The Tomcat container configuration. Set to `""` or `"{}"` to delete the configuration:
        # 
        # - \\`useDefaultConfig\\`: Specifies whether to use a custom configuration. If \\`true\\`, the custom configuration is not used. If \\`false\\`, the custom configuration is used. If you do not use a custom configuration, the following parameter settings do not take effect.
        # 
        # - \\`contextInputType\\`: The access path of the application.
        # 
        #   - \\`war\\`: You do not need to enter a custom path. The access path is the name of the WAR package.
        # 
        #   - \\`root\\`: You do not need to enter a custom path. The access path is \\`/\\`.
        # 
        #   - \\`custom\\`: You need to enter a custom path in the \\`contextPath\\` parameter below.
        # 
        # - \\`contextPath\\`: The custom path. This parameter is required only when \\`contextInputType\\` is set to \\`custom\\`.
        # 
        # - \\`httpPort\\`: The port number. The valid range is 1024 to 65535. Ports smaller than 1024 require root permissions. Because the container is configured with administrator permissions, specify a port number greater than 1024. If you do not configure this, the default port is 8080.
        # 
        # - \\`maxThreads\\`: The size of the connection pool. The default value is 400.
        # 
        #   > This configuration greatly affects application performance. Configure it under professional guidance.
        # 
        # - \\`uriEncoding\\`: The encoding format for Tomcat. Valid values: UTF-8, ISO-8859-1, GBK, and GB2312. If you do not set this, the default is ISO-8859-1.
        # 
        # - \\`useBodyEncoding\\`: Specifies whether to use BodyEncoding for URLs.
        # 
        # - \\`useAdvancedServerXml\\`: Specifies whether to use advanced configuration to customize the \\`server.xml\\` file. If the preceding parameter types and values do not meet your needs, you can use the advanced settings to directly edit the Tomcat \\`Server.xml\\` file.
        # 
        # - \\`serverXml\\`: The content of the custom \\`server.xml\\` text file in the advanced configuration. This takes effect when \\`useAdvancedServerXml\\` is \\`true\\`.
        self.web_container_config = web_container_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.args is not None:
            result['Args'] = self.args

        if self.batch_timeout is not None:
            result['BatchTimeout'] = self.batch_timeout

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.build_pack_id is not None:
            result['BuildPackId'] = self.build_pack_id

        if self.canary_rule_id is not None:
            result['CanaryRuleId'] = self.canary_rule_id

        if self.change_order_desc is not None:
            result['ChangeOrderDesc'] = self.change_order_desc

        if self.command is not None:
            result['Command'] = self.command

        if self.config_mount_descs is not None:
            result['ConfigMountDescs'] = self.config_mount_descs

        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit

        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request

        if self.custom_affinity is not None:
            result['CustomAffinity'] = self.custom_affinity

        if self.custom_agent_version is not None:
            result['CustomAgentVersion'] = self.custom_agent_version

        if self.custom_tolerations is not None:
            result['CustomTolerations'] = self.custom_tolerations

        if self.deploy_across_nodes is not None:
            result['DeployAcrossNodes'] = self.deploy_across_nodes

        if self.deploy_across_zones is not None:
            result['DeployAcrossZones'] = self.deploy_across_zones

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.empty_dirs is not None:
            result['EmptyDirs'] = self.empty_dirs

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        if self.enable_empty_push_reject is not None:
            result['EnableEmptyPushReject'] = self.enable_empty_push_reject

        if self.enable_lossless_rule is not None:
            result['EnableLosslessRule'] = self.enable_lossless_rule

        if self.env_froms is not None:
            result['EnvFroms'] = self.env_froms

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image is not None:
            result['Image'] = self.image

        if self.image_platforms is not None:
            result['ImagePlatforms'] = self.image_platforms

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.init_containers is not None:
            result['InitContainers'] = self.init_containers

        if self.jdk is not None:
            result['JDK'] = self.jdk

        if self.java_start_up_config is not None:
            result['JavaStartUpConfig'] = self.java_start_up_config

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.limit_ephemeral_storage is not None:
            result['LimitEphemeralStorage'] = self.limit_ephemeral_storage

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.local_volume is not None:
            result['LocalVolume'] = self.local_volume

        if self.lossless_rule_aligned is not None:
            result['LosslessRuleAligned'] = self.lossless_rule_aligned

        if self.lossless_rule_delay_time is not None:
            result['LosslessRuleDelayTime'] = self.lossless_rule_delay_time

        if self.lossless_rule_func_type is not None:
            result['LosslessRuleFuncType'] = self.lossless_rule_func_type

        if self.lossless_rule_related is not None:
            result['LosslessRuleRelated'] = self.lossless_rule_related

        if self.lossless_rule_warmup_time is not None:
            result['LosslessRuleWarmupTime'] = self.lossless_rule_warmup_time

        if self.mcpu_limit is not None:
            result['McpuLimit'] = self.mcpu_limit

        if self.mcpu_request is not None:
            result['McpuRequest'] = self.mcpu_request

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.memory_request is not None:
            result['MemoryRequest'] = self.memory_request

        if self.mount_descs is not None:
            result['MountDescs'] = self.mount_descs

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.package_version_id is not None:
            result['PackageVersionId'] = self.package_version_id

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.pvc_mount_descs is not None:
            result['PvcMountDescs'] = self.pvc_mount_descs

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.requests_ephemeral_storage is not None:
            result['RequestsEphemeralStorage'] = self.requests_ephemeral_storage

        if self.runtime_class_name is not None:
            result['RuntimeClassName'] = self.runtime_class_name

        if self.security_context is not None:
            result['SecurityContext'] = self.security_context

        if self.sidecars is not None:
            result['Sidecars'] = self.sidecars

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.startup is not None:
            result['Startup'] = self.startup

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.terminate_grace_period is not None:
            result['TerminateGracePeriod'] = self.terminate_grace_period

        if self.traffic_control_strategy is not None:
            result['TrafficControlStrategy'] = self.traffic_control_strategy

        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy

        if self.uri_encoding is not None:
            result['UriEncoding'] = self.uri_encoding

        if self.use_body_encoding is not None:
            result['UseBodyEncoding'] = self.use_body_encoding

        if self.user_base_image_url is not None:
            result['UserBaseImageUrl'] = self.user_base_image_url

        if self.volumes_str is not None:
            result['VolumesStr'] = self.volumes_str

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        if self.web_container_config is not None:
            result['WebContainerConfig'] = self.web_container_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('BatchTimeout') is not None:
            self.batch_timeout = m.get('BatchTimeout')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('BuildPackId') is not None:
            self.build_pack_id = m.get('BuildPackId')

        if m.get('CanaryRuleId') is not None:
            self.canary_rule_id = m.get('CanaryRuleId')

        if m.get('ChangeOrderDesc') is not None:
            self.change_order_desc = m.get('ChangeOrderDesc')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('ConfigMountDescs') is not None:
            self.config_mount_descs = m.get('ConfigMountDescs')

        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')

        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')

        if m.get('CustomAffinity') is not None:
            self.custom_affinity = m.get('CustomAffinity')

        if m.get('CustomAgentVersion') is not None:
            self.custom_agent_version = m.get('CustomAgentVersion')

        if m.get('CustomTolerations') is not None:
            self.custom_tolerations = m.get('CustomTolerations')

        if m.get('DeployAcrossNodes') is not None:
            self.deploy_across_nodes = m.get('DeployAcrossNodes')

        if m.get('DeployAcrossZones') is not None:
            self.deploy_across_zones = m.get('DeployAcrossZones')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EmptyDirs') is not None:
            self.empty_dirs = m.get('EmptyDirs')

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        if m.get('EnableEmptyPushReject') is not None:
            self.enable_empty_push_reject = m.get('EnableEmptyPushReject')

        if m.get('EnableLosslessRule') is not None:
            self.enable_lossless_rule = m.get('EnableLosslessRule')

        if m.get('EnvFroms') is not None:
            self.env_froms = m.get('EnvFroms')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImagePlatforms') is not None:
            self.image_platforms = m.get('ImagePlatforms')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('InitContainers') is not None:
            self.init_containers = m.get('InitContainers')

        if m.get('JDK') is not None:
            self.jdk = m.get('JDK')

        if m.get('JavaStartUpConfig') is not None:
            self.java_start_up_config = m.get('JavaStartUpConfig')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LimitEphemeralStorage') is not None:
            self.limit_ephemeral_storage = m.get('LimitEphemeralStorage')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('LocalVolume') is not None:
            self.local_volume = m.get('LocalVolume')

        if m.get('LosslessRuleAligned') is not None:
            self.lossless_rule_aligned = m.get('LosslessRuleAligned')

        if m.get('LosslessRuleDelayTime') is not None:
            self.lossless_rule_delay_time = m.get('LosslessRuleDelayTime')

        if m.get('LosslessRuleFuncType') is not None:
            self.lossless_rule_func_type = m.get('LosslessRuleFuncType')

        if m.get('LosslessRuleRelated') is not None:
            self.lossless_rule_related = m.get('LosslessRuleRelated')

        if m.get('LosslessRuleWarmupTime') is not None:
            self.lossless_rule_warmup_time = m.get('LosslessRuleWarmupTime')

        if m.get('McpuLimit') is not None:
            self.mcpu_limit = m.get('McpuLimit')

        if m.get('McpuRequest') is not None:
            self.mcpu_request = m.get('McpuRequest')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('MemoryRequest') is not None:
            self.memory_request = m.get('MemoryRequest')

        if m.get('MountDescs') is not None:
            self.mount_descs = m.get('MountDescs')

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('PackageVersionId') is not None:
            self.package_version_id = m.get('PackageVersionId')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('PvcMountDescs') is not None:
            self.pvc_mount_descs = m.get('PvcMountDescs')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('RequestsEphemeralStorage') is not None:
            self.requests_ephemeral_storage = m.get('RequestsEphemeralStorage')

        if m.get('RuntimeClassName') is not None:
            self.runtime_class_name = m.get('RuntimeClassName')

        if m.get('SecurityContext') is not None:
            self.security_context = m.get('SecurityContext')

        if m.get('Sidecars') is not None:
            self.sidecars = m.get('Sidecars')

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('Startup') is not None:
            self.startup = m.get('Startup')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TerminateGracePeriod') is not None:
            self.terminate_grace_period = m.get('TerminateGracePeriod')

        if m.get('TrafficControlStrategy') is not None:
            self.traffic_control_strategy = m.get('TrafficControlStrategy')

        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')

        if m.get('UriEncoding') is not None:
            self.uri_encoding = m.get('UriEncoding')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        if m.get('UserBaseImageUrl') is not None:
            self.user_base_image_url = m.get('UserBaseImageUrl')

        if m.get('VolumesStr') is not None:
            self.volumes_str = m.get('VolumesStr')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        if m.get('WebContainerConfig') is not None:
            self.web_container_config = m.get('WebContainerConfig')

        return self

