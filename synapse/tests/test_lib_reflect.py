import synapse.lib.base as s_base
import synapse.lib.reflect as s_reflect

import synapse.lib.version as s_version
import synapse.tests.utils as s_t_utils

class Lol: pass
class Foo(Lol): pass

class Bar:
    def __init__(self):
        self.foo = Foo()

    def _syn_reflect(self):
        return s_reflect.getItemInfo(self.foo)

class Echo(s_base.Base):
    def echo(self, args):
        """Echo args back to the caller"""
        return args

    async def mygenr(self, n):
        for i in range(n):
            yield i

class ReflectTest(s_t_utils.SynTest):

    def test_reflect_getClsNames(self):
        foo = Foo()
        names = s_reflect.getClsNames(foo)
        self.isin('synapse.tests.test_lib_reflect.Lol', names)
        self.isin('synapse.tests.test_lib_reflect.Foo', names)

    async def test_first_telemeth(self):
        self.none(getattr(Echo, '_syn_sharinfo_synapse.tests.test_lib_reflect_Echo', None))
        async with self.getTestDmon() as dmon:
            echo = await Echo.anit()
            dmon.share('echo', echo)
            self.none(getattr(echo, '_syn_sharinfo_synapse.tests.test_lib_reflect_Echo', None))
            self.none(getattr(Echo, '_syn_sharinfo_synapse.tests.test_lib_reflect_Echo', None))
            async with await self.getTestProxy(dmon, 'echo') as proxy:
                pass
            self.isinstance(getattr(echo, '_syn_sharinfo_synapse.tests.test_lib_reflect_Echo', None), dict)
            self.isinstance(getattr(Echo, '_syn_sharinfo_synapse.tests.test_lib_reflect_Echo', None), dict)

            sharinfo = getattr(echo, '_syn_sharinfo_synapse.tests.test_lib_reflect_Echo')
            self.eq(sharinfo.get('version'), s_version.version)
            self.eq(sharinfo.get('verstring'), s_version.verstring)

    async def test_full_telemeth(self):
        async with self.getTestDmon() as dmon:
            echo = await Echo.anit()
            dmon.share('echo', echo)
            async with await self.getTestProxy(dmon, 'echo') as proxy:
                mesg = await proxy.t2reflect()
                from pprint import pprint
                pprint(mesg)
                attrs = dir(proxy)
                print(attrs)
                help(proxy)
                help(proxy.echo)
