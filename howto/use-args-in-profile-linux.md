- “exclude_args” は type=“local_only” でのみ使用可能です。 "exclude_args" 内に定義された引数を持つプロセスは “allow_remote” となります。
- "include_args" は type="intercepted" でのみ使用可能です。"include_args" 内に定義された引数を持つプロセスは "intercepted" となり、それ以外のプロセスは "local_only" となります。