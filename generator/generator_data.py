#!/usr/local/bin/python
# -*- coding: utf-8 -*-

data = {
"""Chapter01-0""" : """ 
	<p>Take a look at some of the console programs, such as <code>cp</code> in Linux. They all have a fancy help;
	their input parameters do not depend on any position, and have a human-readable syntax,
	for example:</p>
	<pre><code>
    $ cp --help

    Usage: cp [OPTION]... [-T] SOURCE DEST
        -a, --archive       same as -dR --preserve=all
        -b                  like --backup but does not accept an argument
</code></pre>
	<p>You can implement the same functionality for your program in 10 minutes. And all you need
	is the Boost.ProgramOptions library.</p>
""",

"""Chapter01-1""" : """ 
	<p>If you have been programming in Java, C#, or Delphi, you will definitely miss the ability to
	create containers with the <code>Object</code> value type in C++. The <code>Object</code> class in those languages is
	a basic class for almost all types, so you are able to assign (almost) any value to it at any time.</p>
	<p>Just imagine how great it would be to have such a feature in C++</p>
""",

"""Chapter01-2""" : """ 
	<p>C++03 unions can only hold extremely simple types called Plain Old Data (POD). For
    example in C++03, you cannot store <code>std::string</code> or <code>std::vector</code> in a union.</p>

    <p>Are you aware of the concept of unrestricted unions in C++11? Let me tell you about it
    briefly. C++11 relaxes requirements for unions, but you have to manage the construction
    and destruction of non POD types by yourself. You have to call in-place
    construction/destruction and remember what type is stored in a union. A huge amount of
    work, isn't it?</p>

    <p>Can we have an unrestricted union like variable in C++03 that manages the object lifetime
    and remembers the type it has?</p>
""",

"""Chapter01-3""" : """ 
	<p>Imagine that you are creating a wrapper around some SQL database interface. You decided
	that <code>boost::any</code> will perfectly match the requirements for a single cell of the database
	table. Some other programmer will be using your classes, and his task would be to get a
	row from the database and count the sum of the arithmetic types in a row.</p>
	
	<p>This is what such a code would look like:</p>
	
""",

"""Chapter01-4""" : """ 
	<p>Imagine that we have a function that does not throw an exception and returns a value or
	indicates that an error has occurred. In Java or C# programming languages, such cases are
	handled by comparing a return value from a function value with a <code>null</code> pointer; if it is <code>null</code> then
	an error has occurred. In C++, returning a pointer from a function confuses library users and
	usually requires dynamic memory allocation (which is slow).</p>
""",

"""Chapter01-5""" : """ 
	<p>Let's play a guessing game! What can you tell about the following function?</p>
	<pre><code>
    char* vector_advance(char* val);
</code></pre>

	<p>Should return values be deallocated by the programmer or not? Does the function attempt
    to deallocate the input parameter? Should the input parameter be zero-terminated, or
    should the function assume that the input parameter has a specified width?</p>
	<p>Now, let's make the task harder! Take a look at the following line:</p>
	<pre><code>
    char ( &amp;vector_advance( char (&amp;val)[4] ) )[4];
</code></pre>
	<p>Do not worry. I've also been scratching my head for half an hour before getting an idea of
    what is happening here. vector_advance is a function that accepts and returns an array of
    four elements. Is there a way to write such a function clearly?</p>
""",

"""Chapter01-6""" : """ 
	<p>There is a very nice present for those who like <code>std::pair</code>. Boost has a library called Boost.Tuple.
	It is just like std::pair , but it can also work with triples, quads, and even
    bigger collections of types.</p>
""",

"""Chapter01-7""" : """ 
	<p>If you work with the standard library a lot and use the &lt;algorithm&gt; header, you definitely
    write a lot of functional objects. In C++14, you can use generic lambdas for that. In C++11,
    you only have non generic lambdas. In the earlier versions of the C++ standard, you can
    construct functional objects using adapter functions such as bind1st , bind2nd , ptr_fun ,
    mem_fun , mem_fun_ref , or you can write them by hand (because adapter functions look
    scary). Here is some good news: Boost.Bind can be used instead of ugly adapter functions,
    and it provides a more human-readable syntax.</p>
""",

"""Chapter01-8""" : """ 
	<p>There is often a need to get a readable type name at runtime:</p>
	<pre><code>
	#include &lt;iostream&gt;
    #include &lt;typeinfo&gt;

    template &lt;class T&gt;
    void do_something(const T&amp; x) {
        std::cout &lt;&lt; "T is " &lt;&lt; typeid(T).name() &lt;&lt; std::endl;

        // ...
    }
</code></pre>
    <p>However, the example from earlier is not very portable. It does not work when RTTI is
    disabled, and it does not always produce a nice human-readable name. On some platforms,
    code from earlier will output just <code>i</code> or <code>d</code>.</p>
    <p>Things get worse if we need a type name without stripping the const , volatile , and references...</p>
""",

"""Chapter01-9""" : """ 
	<p>One of the greatest features of the C++11 standard is rvalue references. This feature allows
	us to modify temporary objects, "stealing" resources from them. As you can guess, the C++03
	standard has no rvalue references, but using the Boost.Move library you can write some
	portable code that uses them, and even more, you actually get started with the emulation of
	move semantics.</p>
""",

"""Chapter01-10""" : """ 
	<p>You have almost certainly encountered certain situations, where a class owns some
    resources that must not be copied for technical reasons:</p>
	<pre><code>
    class descriptor_owner {
        void* descriptor_;

    public:
        explicit descriptor_owner(const char* params);

        ~descriptor_owner() {
            system_api_free_descriptor(descriptor_);
        }
    };
</code></pre>
	<p>The C++ compiler in the preceding example generates a copy constructor and an assignment
    operator, so the potential user of the descriptor_owner class will be able to create the
    following awful things:</p>
	<pre><code>
    descriptor_owner d1("O_o");
    descriptor_owner d2("^_^");

    // Descriptor of d2 was not correctly freed
    d2 = d1;

    // destructor of d2 will free the descriptor
    // destructor of d1 will try to free already freed descriptor
</code></pre>
""",

"""Chapter01-11""" : """ 
	<p>Now imagine the following situation: we have a resource that cannot be copied, which should
	be correctly freed in a destructor, and we want to return it from a function:</p>
	<pre><code>
    descriptor_owner construct_descriptor() {
        return descriptor_owner("Construct using this string");
    }
</code></pre>

	<p>Actually, you can work around such situations using the swap method:</p>
    <pre><code>
    void construct_descriptor1(descriptor_owner& ret) {
        descriptor_owner("Construct using this string").swap(ret);
    }
</code></pre>
	<p>But such a workaround won't allow us to use descriptor_owner in STL or Boost containers.
	And by the way, it looks awful!</p>
""",

"""Chapter01-12""" : """ 
	<p>C++11 has a bunch of new cool algorithms in &lt;algorithm&gt; header. C++14 has even more
    algorithms. If you're stuck with the pre-C++11 compiler, you have to write those from
    scratch. For example, if you wish to output characters from 65 to 125 code points, you have
    to write the following code on a pre-C++11 compiler:</p>
""",


"""Chapter02-0""" : """ 
	<p>Sometimes we are required to dynamically allocate memory and construct a
	class in that memory. And, that's where the troubles start. Have a look at the following code:</p>
    <pre><code>
    void foo1() {
        foo_class* p = new foo_class("Some initialization data");
        bool something_else_happened = some_function1(p);
        if (something_else_happened) {
            delete p;
            return false;
        }

        some_function2(p);
        delete p;
        return true;
    }
</code></pre>
	<p>This code looks correct at first glance. But, what if <code>some_function1()</code> or <code>some_function2()</code>
	throws an exception? In that case, <code>p</code> won't be deleted. Let's fix it in the
	following way:</p>
    <pre><code>
    void foo2() {
        foo_class* p = new foo_class("Some initialization data");
        try {
            bool something_else_happened = some_function1(p);
            if (something_else_happened) {
                delete p;
                return false;
            }

            some_function2(p);
        } catch (...) {
            delete p;
            throw;
        }

        delete p;
        return true;
    }
</code></pre>
	<p>Now the code is ugly and hard to read but is correct. Maybe we can do better than this.</p>
""",


"""Chapter02-1""" : """ 
	<p>Imagine that you have some dynamically allocated structure containing data, and you want
	to process it in different execution threads. The code to do this is as follows:</p>
	<pre><code>
    #include &lt;boost/thread.hpp&gt;
    #include &lt;boost/bind.hpp&gt;
    void process1(const foo_class* p);
    void process2(const foo_class* p);
    void process3(const foo_class* p);

    void foo1() {
        while (foo_class* p = get_data()) // C way
        {
            // There will be too many threads soon, see
            // recipe 'Executing different tasks in parallel'
            // for a good way to avoid uncontrolled growth of threads
            boost::thread(boost::bind(&amp;process1, p))
                .detach();
            boost::thread(boost::bind(&amp;process2, p))
                .detach();
            boost::thread(boost::bind(&amp;process3, p))
                .detach();

            // delete p; Oops!!!!
        }
    }
</code></pre>
	<p>We cannot deallocate <code>p</code> at the end of the while loop because it can still be used by threads
	that run process functions. Process functions cannot delete <code>p</code> because they do not know that
	other threads are not using it anymore.</p>
""",

"""Chapter02-2""" : """ 
	<p>We already saw how to manage pointers to a resource in the Managing pointers to classes
	that do not leave scope recipe. But, when we deal with arrays, we need to call <code>delete[]</code>
	instead of a simple delete , otherwise there will be a memory leak. Have a look at the
	following code:</p>
	<pre><code>
    void may_throw1(const char* buffer);
    void may_throw2(const char* buffer);

    void foo() {
        // we cannot allocate 10MB of memory on stack,
        // so we allocate it on heap
        char* buffer = new char[1024 * 1024 * 10];

        // Here comes some code, that may throw
        may_throw1(buffer);
        may_throw2(buffer);

        delete[] buffer;
    }
</code></pre>
""",

"""Chapter02-3""" : """ 
	<p>We continue coping with pointers, and our next task is to reference count an array. Let's
	take a look at a program that gets some data from the stream and processes it in different
	threads. The code to do this is as follows:</p>
	<pre><code>
    #include &lt;cstring&gt;
    #include &lt;boost/thread.hpp&gt;
    #include &lt;boost/bind.hpp&gt;

    void do_process(const char* data, std::size_t size);
    void do_process_in_background(const char* data, std::size_t size) {
        // We need to copy data, because we do not know,
        // when it will be deallocated by the caller
        char* data_cpy = new char[size];
        std::memcpy(data_cpy, data, size);

        // Starting thread of execution to process data
        boost::thread(boost::bind(&amp;do_process, data_cpy, size))
            .detach();

        // We cannot delete[] data_cpy, because
        // do_process1 or do_process2 may still work with it
    }
</code></pre>
	<p>Just the same problem that occurred in the <a href="javascript:editor.download('Chapter03', 1)">Reference counting of pointers to classes used across methods</a>
	recipe.</p>
""",

"""Chapter02-4""" : """ 
	<p>Consider the situation when you are developing a library that has its API declared in the
    header files and implementation in the source files. This library shall have a function that
    accepts any functional objects. Take a look at the following code:</p>
	<pre><code>
    // Required for std::unary_function&lt;&gt; template
    #include &lt;functional&gt;

    // making a typedef for function pointer accepting int
    // and returning nothing
    typedef void (*func_t)(int);

    // Function that accepts pointer to function and
    // calls accepted function for each integer that it has
    // It cannot work with functional objects :(
    void process_integers(func_t f);

    // Functional object
    class int_processor: public std::unary_function&lt;int, void&gt; {
        const int min_;
        const int max_;
        bool& triggered_;

    public:
        int_processor(int min, int max, bool& triggered)
            : min_(min)
            , max_(max)
            , triggered_(triggered)
        {}

        void operator()(int i) const {
            if (i &lt; min_ || i &gt; max_) {
                triggered_ = true;
            }
        }
    };
</code></pre>
""",

"""Chapter02-5""" : """ 
	<p>We are continuing with the previous example, and now we want to pass a pointer to a function
	in our <code>process_integeres()</code> method. Shall we add an overload for just function pointers,
	or is there a more elegant way?</p>
""",

"""Chapter02-6""" : """ 
	<p>We are continuing with the previous example, and now we want to use a lambda function with
	our <code>process_integers()</code> method.</p>
""",

"""Chapter02-7""" : """ 
	<p>There are such cases when we need to store pointers in the container. The examples are:
	storing polymorphic data in containers, forcing fast copy of data in containers, and strict
	exception requirements for operations with data in containers. In such cases, the C++
	programmer has the following choices:</p>

	<p>* Store pointers in containers and take care of their destructions using the operator
	delete. Such an approach is error prone and requires a lot of writing.</p>

	<p>* Store smart pointers in containers. For the C++03 you'll have to use <code>std::auto_ptr</code>. However the
	<code>std::auto_ptr</code> class is deprecated, and it is not recommended to use it in containers. For the C++11 version
	you'll have to use <code>std::unique_ptr</code>. This solution is a good one, but it cannot be used in C++03, and you still need to
	write a comparator functional object.</p>

	<p>* Use Boost.SmartPtr in the container. This solution is portable, but you still need to write comparators, and it adds
	performance penalties (an atomic counter requires additional memory,
	and its increments/decrements are not as fast as nonatomic operations).</p>
""",

"""Chapter02-8""" : """ 
	<p>If you were dealing with languages such as Java, C#, or Delphi, you were obviously using the
	<code>try{} finally{}</code> construction or <code>scope(exit)</code> in the D programming language. Let me
	briefly describe to you what do these language constructions do.</p>

	<p>When a program leaves the current scope via return or exception, code in the finally or
	scope(exit) blocks is executed. This mechanism is perfect for implementing the RAII
	pattern as shown in the following code snippet:</p>
	<pre><code>
    // Some pseudo code (suspiciously similar to Java code)
    try {
        FileWriter f = new FileWriter("example_file.txt");
        // Some code that may trow or return
        // ...
    } finally {
        // Whatever happened in scope, this code will be executed
        // and file will be correctly closed
        if (f != null) {
            f.close()
        }
    }
</code></pre>
	<p>Is there a way to do such a thing in C++?</p>
""",


"""Chapter02-9""" : """ 
	<p>Let's take a look at the following example. We have some base class that has virtual functions
	and must be initialized with reference to the <code>std::ostream</code> object:</p>
	<pre><code>
    #include &lt;boost/noncopyable.hpp&gt;
    #include &lt;sstream&gt;
    class tasks_processor: boost::noncopyable {
        std::ostream& log_;
    public:
        explicit tasks_processor(std::ostream& log)
            : log_(log)
        {}
    };
</code></pre>

	<p>We also have a derived class that has a std::ostream object:</p>
	<pre><code>
    class fake_tasks_processor: public tasks_processor {
        std::ostringstream logger_;

    public:
        fake_tasks_processor()
            : tasks_processor(logger_) // Oops! logger_ does not exist here
            , logger_()
        {}
    };
</code></pre>
	<p>This is not a very common case in programming, but when such mistakes happen, it is not
	always simple to get the idea of bypassing it. Some people try to bypass it by changing the
	order of <code>logger_</code> and the base type initialization:</p>
    <pre><code>
        fake_tasks_processor()
            : logger_() // Oops! logger_ still will be constructed AFTER tasks_processor
            , tasks_processor(logger_)
        {}
</code></pre>
	<p>It won't work as they expect because direct base classes are initialized before nonstatic
	data members, regardless of the order of the member initializers.</p>
""",




"""Chapter03-0""" : """ 
	<p>Converting strings to numbers in C++ makes a lot of people depressed because of its
	inefficiency and user unfriendliness. Let's see how string 100 can be converted to <code>int</code>:</p>
	<pre><code>
    #include &lt;sstream&gt;
    std::istringstream iss("100");
    int i;
    iss >> i;
    // And now, 'iss' variable will get in the way all the time,
    // till end of the scope
    // It is better not to think, how many unnecessary operations,
    // virtual function calls and memory allocations occurred
    // during those operations
</code></pre>
	<p>C methods are not much better:</p>
	<pre><code>
    #include &lt;cstdlib&gt;
    char * end;
    int i = std::strtol ("100", &amp;end, 10);
    // Did it converted all the value to int, or stopped somewhere
    // in the middle?
    // And now we have 'end' variable will getting in the way
    // By the way, we want an integer, but strtol returns long
    // int... Did the converted value fit in int?
</code></pre>
""",

"""Chapter03-1""" : """ 
	<p>In this recipe we will continue discussing lexical conversions, but now we will be converting
	numbers to strings using Boost.LexicalCast . And as usual, <code>boost::lexical_cast</code>
	will provide a very simple way to convert the data.</p>
""",

"""Chapter03-2""" : """ 
	<p>You might remember situations where you wrote something like the following code:</p>
	<pre><code>
    void some_function(unsigned short param);
    int foo();
    // Somewhere in code
    // Some compilers may warn that int is being converted to
    // unsigned short and that there is a possibility of losing
    // data
    some_function(foo());
</code></pre>
	<p>Usually, programmers just ignore such warnings by implicitly casting to unsigned short
	datatype, as demonstrated in the following code snippet:</p>
    <pre><code>
    // Warning suppressed. Looks like a correct code
    some_function(
        static_cast&lt;unsigned short&gt;(foo())
    );
</code></pre>
	<p>But this may make it extremely hard to detect errors. Such errors may exist in code for years
	before they get caught:</p>
	<pre><code>
    // Returns -1 if error occurred
    int foo() {
        if (some_extremely_rare_condition()) {
            return -1;
        } else if (another_extremely_rare_condition()) {
            return 1000000;
        }
        return 65535;
    }
</code></pre>
""",


"""Chapter03-3""" : """ 
	<p>There is a feature in Boost.LexicalCast that allows users to use their own types in
	lexical_cast . This feature just requires the user to write the correct <code>std::ostream</code>
	and <code>std::istream</code> operators for their types.</p>
""",

"""Chapter03-4""" : """ 
	<p>Imagine that some programmer designed an awful interface as follows (this is a good example
	of how interfaces should not be written):</p>
	<pre><code>
    struct object {
        virtual ~object() {}
    };

    struct banana: public object {
        void eat() const {}
        virtual ~banana(){}
    };

    struct pidgin: public object {
        void fly() const {}
        virtual ~pidgin(){}
    };

    object* try_produce_banana();
</code></pre>
	<p>Our task is to make a function that eats bananas, and throws exceptions if something
	instead of banana came along (eating pidgins gross!). If we dereference a value returned
	by the <code>try_produce_banana()</code> function, we are getting in danger of dereferencing
	a null pointer.</p>
""",


"""Chapter03-5""" : """ 
	<p>Here's a problem:</p>
	<p>* You have a class named some_class :</p>

	<pre><code>
    struct base {
        virtual void some_methods() = 0;
        virtual ~base();
    };
    
    struct derived: public base {
        void some_methods() /*override*/;
        virtual void derived_method() const;
        ~derived() /*override*/;
    };
</code></pre>
	<p>You have a third-party API that returns constructed derived by shared pointer
    to base and accepts shared pointer to const derived in other functions:</p>
	<pre><code>
    #include &lt;boost/shared_ptr.hpp&gt;
    boost::shared_ptr&lt;const base&gt; construct_derived();
    void im_accepting_derived(boost::shared_ptr&lt;const derived&gt; p);
</code></pre>
	<p>You have a third-party API that returns constructed derived by shared pointer
    to base and accepts shared pointer to const derived in other functions:</p>
	<pre><code>
    void trying_hard_to_pass_derived() {
        boost::shared_ptr&lt;const base&gt; d = construct_derived();

        // Oops! Compile time error:
        // ‘const struct base’ has no member named ‘derived_method’.
        d-&gt;derived_method();

        // Oops! Compile time error:
        // could not convert ‘d’ to ‘boost::shared_ptr&lt;const derived&gt;’.
        im_accepting_derived(d);
    }
</code></pre>
""",

"""Chapter03-6""" : """ 
	<p>Imagine that some programmer designed such an awful interface as follows (this is a good
    example of how interfaces should not be written):</p>
	<pre><code>
    struct object {
        virtual ~object() {}
    };

    struct banana: public object {
        void eat() const {}
        virtual ~banana(){}
    };

    struct penguin: public object {
        bool try_to_fly() const {
            return false; // penguins do not fly
        }
        virtual ~penguin(){}
    };

    object* try_produce_banana();
</code></pre>
    <p>Our task is to make a function that eats bananas, and throws exceptions if something
    different came instead of banana ( try_produce_banana() may return nullptr )so if we
    dereference a value returned by it without checking we are in danger of dereferencing a
    null pointer.</p>
""",

"""Chapter03-7""" : """ 
	<p>It is a common task to parse a small text. And such situations are always a dilemma: shall we
	use some third-party professional tools for parsing such as Bison or ANTLR, or shall we try to
	write it by hand using only C++ and STL? The third-party tools are good for handling the parsing
	of complex texts and it is easy to write parsers using them, but they require additional tools
	for creating C++ or C code from their grammar, and add more dependencies to your project.
	Handwritten parsers are usually hard to maintain, but they require nothing except C++ compiler.</p>

	<p>Let's start with a very simple task to parse a date in ISO format as follows:</p>
	<pre><code>
        YYYY-MM-DD
</code></pre>
	<p>The following are the examples of possible input:</p>
	<pre><code>
        2013-03-01
        2012-12-31 // (woo-hoo, it almost a new year!)
</code></pre>
""",

"""Chapter03-8""" : """ 
	<p>In the previous recipe we were writing a simple parser for dates. Imagine that some time
	has passed and the task has changed. Now we need to write a date-time parser that will
	support multiple input formats plus zone offsets. So now our parser should understand the
	following inputs:</p>
	<pre><code>
        2012-10-20T10:00:00Z        // date time with zero zone offset
        2012-10-20T10:00:00         // date time with unspecified zone offset
        2012-10-20T10:00:00+09:15   // date time with zone offset
        2012-10-20-09:15            // date time with zone offset
        10:00:09+09:15              // time with zone offset
</code></pre>
""",


"""Chapter04-0""" : """ 
	<p>Let's imagine that we are writing some serialization function that stores values in buffer of a
	specified size:</p>
	<pre><code>
    #include &lt;cstring&gt;
    #include &lt;boost/array.hpp&gt;

    // C++17 has std::byte out of the box!
    // Unfortunately this is as C++03 example.
    typedef unsigned char byte_t;

    template &lt;class T, std::size_t BufSizeV&gt;
    void serialize_bad(const T& value, boost::array&lt;byte_t, BufSizeV&gt;&amp; buffer)
    {
        // TODO: check buffer size.
        std::memcpy(&amp;buffer[0], &amp;value, sizeof(value));
    }
</code></pre>

	<p>This code has the following problems:</p>
	<p>* The size of the buffer is not checked, so it may overflow</p>
	<p>* This function can be used with non-plain old data (POD) types, which would lead to incorrect behavior</p>

	<p>We may partially fix it by adding some asserts, for example:</p>
	<pre><code>
    template &lt;class T, std::size_t BufSizeV&gt;
    void serialize(const T&amp; value, boost::array&lt;byte_t, BufSizeV&gt;&amp; buffer) {
        assert(BufSizeV &gt;= sizeof(value));
        // TODO: fixme
        std::memcpy(&amp;buffer[0], &amp;value, sizeof(value));
    }
</code></pre>
	<p>But, this is a bad solution. The <code>BufSizeV</code> and <code>sizeof(value)</code> values are known at compile
	time, so we can potentially make this code to fail compilation if the buffer is too small, instead
	of having a runtime assert (which may not trigger during debug, if function was not called, and
	may even be optimized out in release mode, so very bad things may happen).</p>
""",

"""Chapter04-1""" : """ 
	<p>It's a common situation, when we have a templated class that implements some functionality.
	Have a look at the following code snippet:</p>
	<pre><code>
    // Generic implementation
    template &lt;class T&gt;
    class data_processor {
        double process(const T&amp; v1, const T&amp; v2, const T&amp; v3);
    };
</code></pre>
	<p>After execution of the preceding code, we have additional two optimized versions of that class,
	one for integral, and another for real types:</p>
	<pre><code>
    // Integral types optimized version
    template &lt;class T&gt;
    class data_processor {
        typedef int fast_int_t;
        double process(fast_int_t v1, fast_int_t v2, fast_int_t v3);
    };

    // SSE optimized version for float types
    template &lt;class T&gt;
    class data_processor {
        double process(double v1, double v2, double v3);
    };
</code></pre>
	<p>Now the question: How to make the compiler to automatically choose the correct class for a
    specified type?</p>
""",

"""Chapter04-2""" : """ 
	<p>We continue working with Boost metaprogramming libraries. In the previous recipe, we saw
	how to use <code>enable_if_c</code> with classes, now it is time to take a look at its usage in template
	functions. Consider the following example.</p>

	<p>Initially, we had a template function that works with all the available types:</p>
	<pre><code>
        template &lt;class T&gt;
        T process_data(const T&amp; v1, const T&amp; v2, const T&amp; v3);
</code></pre>
	Now that we write code using process_data function, we use an optimized process_data
	version for types that do have an <code>operator +=</code> function:
	<pre><code>
        template &lt;class T&gt;
        T process_data_plus_assign(const T&amp; v1, const T&amp; v2, const T&amp; v3);
</code></pre>
	<p>But, we do not want to change the already written code; instead whenever it is possible, we
	want to force the compiler to automatically use optimized function in place of the default one.</p>
""",

"""Chapter04-3""" : """ 
	<p>We have now seen examples of how we can choose between functions without
	<code>boost::enable_if_c</code> usage. Let's consider the following example, where we have a generic
	method for processing POD datatypes:</p>
	<pre><code>
    #include &lt;boost/static_assert.hpp&gt;
    #include &lt;boost/type_traits/is_pod.hpp&gt;

    // Generic implementation
    template &lt;class T&gt;
    T process(const T&amp; val) {
        BOOST_STATIC_ASSERT((boost::is_pod&lt;T&gt;::value));
        // ...
    }
</code></pre>

	<p>And, we have the same function optimized for sizes 1, 4, and 8 bytes. How do we rewrite
	process function, so that it can dispatch calls to optimized versions?</p>
""",


"""Chapter04-4""" : """ 
	<p>We need to implement a type trait that returns <code>true</code> if the <code>std::vector</code> type is passed to it
	as a template parameter.</p>
""",

"""Chapter04-5""" : """ 
	<p>Imagine that we are working with classes from different vendors that implement different
	amounts of arithmetic operations and have constructors from integers. And, we do want to
	make a function that increments by one when any class is passed to it. Also, we want this
	function to be effective! Take a look at the following code:</p>
	<pre><code>
    template &lt;class T&gt;
    void inc(T&amp; value) {
        // TODO:
        // call ++value
        // or call value++
        // or value += T(1);
        // or value = value + T(1);
    }
</code></pre>
""",


"""Chapter04-6""" : """ 
	<p>In the previous recipes, we saw some examples on <code>boost::bind</code> usage. It is a good and
	useful tool with a small drawback; it is hard to store <code>boost::bind</code> metafunction's functor
	as a variable in C++03.</p>
	<pre><code>
    #include &lt;functional&gt;
    #include &lt;boost/bind.hpp&gt;
    const ??? var = boost::bind(std::plus&lt;int&gt;(), _1, _1);
</code></pre>
	<p>In C++11, we can use auto keyword instead of <code>???</code> , and that will work. Is there a way to
	do it in C++03?</p>
""",


"""Chapter05-0""" : """ 
	<p>On modern multi-core compilers, to achieve maximal performance (or just to provide a good
	user experience), programs usually must use multiple execution threads. Here is a motivating
	example in which we need to create and fill a big file in a thread that draws the user interface:</p>
	<pre><code>
    #include &lt;algorithm&gt;
    #include &lt;fstream&gt;
    #include &lt;iterator&gt;

    void set_not_first_run();
    bool is_first_run();

    // Function, that executes for a long time
    void fill_file_with_data(char fill_char, std::size_t size, const char* filename) {
        std::ofstream ofs(filename);
        std::fill_n(std::ostreambuf_iterator&lt;char&gt;(ofs), size, fill_char);
        set_not_first_run();
    }

    // ...
    // Somewhere in thread that draws a user interface
    if (is_first_run()) {
        // This will be executing for a long time during which
        // user's interface will freeze.
        fill_file_with_data(0, 8 * 1024 * 1024, "save_file.txt");
    }
</code></pre>
""",

"""Chapter05-1""" : """ 
	<p>Now that we know how to start execution threads, we want to have access to some common
	resources from different threads:</p>
	<pre><code>
    #include &lt;cassert&gt;
    #include &lt;cstddef&gt;
    // In previous recipe we included
    // &lt;boost/thread.hpp&gt;, which includes all
    // the classes of Boost.Thread
    #include &lt;boost/thread/thread.hpp&gt;

    int shared_i = 0;

    void do_inc() {
        for (std::size_t i = 0; i &lt; 30000; ++i) {
            // do some work
            // ...
            const int i_snapshot = ++ shared_i;
            // do some work with i_snapshot
            // ...
        }
    }

    void do_dec() {
        for (std::size_t i = 0; i &lt; 30000; ++i) {
            // do some work
            // ...
            const int i_snapshot = -- shared_i;
            // do some work with i_snapshot
            // ...
        }
    }

    void run() {
        boost::thread t1(&amp;do_inc);
        boost::thread t2(&amp;do_dec);

        t1.join();
        t2.join();

        // assert(shared_i == 0); // Oops!
        std::cout &lt;&lt; "shared_i == " &lt;&lt; shared_i;
    }
</code></pre>
	<p>This <code>'Oops!'</code> is not written there accidentally. For some people it will be a surprise, but there
	is a big chance that shared_i won't be equal to 0:</p>
	<pre><code>
        shared_i == 19567
</code></pre>

	<p>And it will get even worse in cases when a common resource has some non-trivial classes;
	segmentation faults and memory leaks may (and will) occur.
	We need to change the code so that only one thread modifies the shared_i variable at a
	single moment of time and so that all of the processor and compiler optimizations that inflict
	multithreaded code are bypassed.</p>
""",

"""Chapter05-2""" : """ 
	<p>In the previous recipe, we saw how to safely access a common resource from different
	threads. But in that recipe, we were doing two system calls (in locking and unlocking the
	mutex) just to get the value from an integer:</p>
	<pre><code>
    { // Critical section begin
        boost::lock_guard&lt;boost::mutex&gt; lock(i_mutex);
        i_snapshot = ++ shared_i;
    } // Critical section end
</code></pre>

	<p>This looks lame and slow! Can we make the code from the previous recipe better?</p>
""",

"""Chapter05-3""" : """ 
	<p>Let's call the functional object that takes no arguments a task.</p>
	<pre><code>
    typedef boost::function&lt;void()&gt; task_t;
</code></pre>
	<p>Now, imagine a situation where we have threads that post tasks and threads that execute
	posted tasks. We need to design a class that can be safely used by both types of thread. This
	class must have methods for getting a task (or blocking and waiting for a task until it is posted
	by another thread), checking and getting a task if we have one (returning an empty task if no
	tasks remain), and a method to post tasks.</p>
""",

"""Chapter05-4""" : """ 
	<p>Imagine that we are developing some online services. We have a map of registered users
	with some properties for each user. This set is accessed by many threads, but it is very rarely
	modified. All operations with the following set are done in a thread-safe manner via acquireing an unique lock on the mutex.</p>

	<p>But any operation, even getting/reading
	resources will result in waiting on a locked mutex; therefore, this class will become a
	bottleneck very soon.</p>

	<p>Can we fix it?</p>
""",

"""Chapter05-5""" : """ 
	<p>Let's take a glance at the recipe <a href="javascript:editor.download('Chapter05', 3)">Creating a work_queue class</a>. Each task there can be
	executed in one of many threads and we do not know which one. Imagine that we want to
	send the results of an executed task using some connection.</p>
	<pre><code>
    #include &lt;boost/noncopyable.hpp&gt;
    class connection: boost::noncopyable {
    public:
        // Opening a connection is a slow operation
        void open();

        void send_result(int result);
        // Other methods
        // ...
    };
</code></pre>

	<p>We have the following solutions:</p>
	<p>* Open a new connection when we need to send the data (which is slow)</p>
	<p>* Have a single connection for all the threads and wrap them in mutex
	(which is also slow)</p>
	<p>* Have a pool of connections, get a connection from it in a thread-safe manner
	and use it (a lot of coding is required, but this solution is fast)</p>
	<p>* Have a single connection per thread (fast and simple to implement)</p>

	<p>So, how can we implement the last solution?</p>
""",

"""Chapter05-6""" : """ 
	<p>Sometimes, we need to kill a thread that ate too many resources or that is just executing for
	too long. For example, some parser works in a thread (and actively uses Boost.Thread),
	but we already have the required amount of data from it, so parsing can be stopped. All we
	have is:</p>
	<pre><code>
    boost::thread parser_thread(&amp;do_parse);

    // Some code goes here
    // ...
    if (stop_parsing) {
        // no more parsing required
        // TODO: stop parser
    }
</code></pre>
	<p>How can we do it?</p>
""",

"""Chapter05-7""" : """ 
	<p>Those readers who were trying to repeat all the examples by themselves or those who were
	experimenting with threads must already be bored with writing the following code to launch
	threads:</p>
	<pre><code>
    boost::thread t1(&amp;some_function);
    boost::thread t2(&amp;some_function);
    boost::thread t3(&amp;some_function);
    // ...
    t1.join();
    t2.join();
    t3.join();
</code></pre>
	<p>Maybe there is a better way to do this?</p>
""",

"""Chapter05-8""" : """ 
	<p>Imagine that we are designing a safety-critical class that is used from multiple threads,
receives answers from a server, postprocesses them, and outputs the response:</p>
	<pre><code>
    struct postprocessor {
        typedef std::vector&lt;std::string&gt; answer_t;

        // Concurrent calls on the same variable are safe.
        answer_t act(const std::string&amp; in) const {
            if (in.empty()) {
                // Extremely rare condition.
                return read_defaults();
            }
            // ...
        }
    };
</code></pre>
	<p>Note the <code>return read_defaults();</code> line. There may be situations when server does not
respond because of networking issues or some other problems. In those cases, we attempt to
read defaults from file:</p>
	<pre><code>
    // Executes for a long time.
    std::vector&lt;std::string&gt; read_defaults();
</code></pre>
	<p>From the preceding code, we hit the problem: the server may be unreachable for some
noticeable time, and for all that time we'll be rereading the file on each act call. This
significantly affects performance.</p>
    <p>So, we have to concurrent-safely read and store the data in the current instance on the first
remote server failure and do not read it again on the next failures. There are many ways to
do that, but let's look at the most right one.</p>
""",

"""Chapter05-9""" : """ 
	<p>For the next few paragraphs, you'll be one of the people who write games. Congratulations,
you can play at work!</p>
	<p>You're developing a server and you have to write code for exchanging loot between two
users:</p>
	<pre><code>
    class user {
        boost::mutex loot_mutex_;
        std::vector&lt;item_t&gt; loot_;
    public:
        // ...
        void exchange_loot(user&amp; u);
    };
</code></pre>
	<p>Each user action could be concurrently processed by different threads on a server, so you
have to guard the resources by mutexes. The junior developer tried to deal with the
problem, but his solution does not work:</p>
	<pre><code>
    void user::exchange_loot(user& u) {
        // Terribly wrong!!! ABBA deadlocks.
        boost::lock_guard&lt;boost::mutex&gt; l0(loot_mutex_);
        boost::lock_guard&lt;boost::mutex&gt; l1(u.loot_mutex_);
        loot_.swap(u.loot_);
    }
</code></pre>
	<p>The issue in the preceding code is a well-known ABBA deadlock problem. Imagine that
thread 1 locks mutex A and thread 2 locks mutex B. And now thread 1 attempts to lock the
already locked mutex B and thread 2 attempts to lock the already locked mutex A. This
results in two threads locked for infinity by each other, as they need a resource locked by
other thread to proceed while the other thread waits for a resource owned by the current
thread.</p>
	<p>Now, if user1 and user2 call <code>exchange_loot</code> for each other concurrently, then we may end
up with a situation that <code>user1.exchange_loot(user2)</code> has locked
<code>user1.loot_mutex_</code> and <code>user2.exchange_loot(user1)</code> has locked
<code>user2.loot_mutex_</code>. Now <code>user1.exchange_loot(user2)</code> waits for infinity in attempt to lock
<code>user2.loot_mutex_</code> and <code>user2.exchange_loot(user1)</code> waits for infinity in an attempt
to lock <code>user1.loot_mutex_</code>.</p>
""",

"""Chapter06-0""" : """ 
	<p>First of all, let's take care of the class that will hold all the tasks and provide methods for their
	execution. We were already doing something like this in the <a href="javascript:editor.download('Chapter05', 3)">Creating a work_queue class</a>
	recipe, but some of the following problems were not addressed:</p>
	<p>* A task may throw an exception that leads a call to std::terminate</p>
	<p>* An interrupted thread may not notice interruption but will finish its task and interrupt
	only during the next task (which is not what we wanted; we wanted to interrupt the
	previous task)</p>
	<p>* Our work_queue class was only storing and returning tasks, but we need to add
	methods for executing existing tasks</p>
	<p>* We need a way to stop processing the tasks</p>
""",

"""Chapter06-1""" : """ 
	<p>It is a common task to check something at specified intervals; for example, we need to check
	some session for an activity once every 5 seconds. There are two popular solutions to such
	a problem:</p>
	<p>* The bad solution creates a thread that does the checking and then sleeps for 5
seconds. This is a lame solution that eats a lot of system resources and scales
badly.</p>
	<p>* The right solution uses system specific APIs for manipulating timers
asynchronously. This is a better solution, that requires some work and is not
portable, unless you use Boost.Asio.</p>
""",

"""Chapter06-2""" : """ 
	<p>Receiving or sending data by network is a slow operation. While packets are received by the
machine, and while OS verifies them and copies the data to the user-specified buffer,
multiple seconds may pass.</p>
	<p>We may do a lot of work rather than waiting! Let's modify our tasks_processor class so
that it would be capable of sending and receiving data in an asynchronous manner. In
nontechnical terms, we ask it to receive at least N bytes from the remote host and after that
is done, call our functor. By the way, do not block on this call. Those readers who know
about libev, libevent, or Node.js may find a lot of familiar things in this recipe.</p>
""",

"""Chapter06-3""" : """ 
	<p>A server-side working with a network often looks like a sequence where we first get the
new connection, read data, then process it, and then send the result. Imagine that we are
creating some kind of authorization server that must process huge amount of requests per
second. In that case, we need to accept, receive, send asynchronously, and process tasks in
multiple threads.</p>
	<p>In this recipe, we'll see how to extend our tasks_processor class to accept and process
incoming connections, and, in the next recipe, we'll see how to make it multithreaded.</p>
""",

"""Chapter06-4""" : """ 
	<p>Now it is time to make our <code>tasks_queue</code> process tasks in multiple threads. How hard could
	this be?</p>
""",

"""Chapter06-5""" : """ 
	<p>Sometimes there is a requirement to process tasks within a specified time interval. Compared
	to previous recipes, where we were trying to process tasks in the order of their appearance in
	the queue, this is a big difference.</p>
	<p>Consider an example where we are writing a program that connects two subsystems, one of
	which produces data packets and the other writes modified data to the disk (something like
	this can be seen in video cameras, sound recorders, and other devices). We need to process
	data packets one by one, smoothly with the least jitter, and in multiple threads.</p>
	<p>Our previous tasks_queue was bad at processing tasks in a specified order, so how can we solve this?</p>
""",

"""Chapter06-6""" : """ 
	<p>In multithreaded programming, there is an abstraction called barrier. It stops execution
	of threads that reach it until the requested number of threads are not blocked on it. After that,
	all the threads are released and they continue with their execution.</p>

	<p>For example, we want to process different parts of the data in different threads and then send the data:</p>
	<pre><code>
    void runner(std::size_t thread_index, boost::barrier&amp; data_barrier, data_t&amp; data) {
        for (std::size_t i = 0; i &lt; 1000; ++ i) {
            fill_data(data.at(thread_index));
            data_barrier.wait();

            if (!thread_index) {
                compute_send_data(data);
            }

            data_barrier.wait();
        }
    }
</code></pre>
	<p>The <code>data_barrier.wait()</code> method blocks until all the threads fill the data. After that,
	all the threads are released; the thread with the index 0 will compute data to be sent using
	<code>compute_send_data(data)</code>, while others are again waiting at the barrier.</p>

	<p>Looks lame, isn't it?</p>
""",

"""Chapter06-7""" : """ 
	<p>Processing exceptions is not always trivial and may consume a lot of time. Consider the
situation when an exception must be serialized and sent by the network. This may take
milliseconds and a few thousands of lines of code. After the exception is caught, it is not
always the best time and place to process it.</p>
	<p>Can we store exceptions and delay their processing?</p>
""",

"""Chapter06-8""" : """ 
	<p>When writing some server application (especially for Linux OS), catching and processing
the signals is required. Usually, all the signal handlers are set up at server start and do not
change during the application's execution.</p>
	<p>The goal of this recipe is to make our <code>tasks_processor</code> class capable of processing signals.</p>
""",

"""Chapter07-0""" : """ 
	<p>This is a pretty common task. We have two non-Unicode or ANSI character strings:</p>
	<pre><code>
    #include &lt;string&gt;
    std::string str1 = "Thanks for reading me!";
    std::string str2 = "Thanks for reading ME!";
</code></pre>
	<p>We need to compare them in a case-insensitive manner. There are a lot of methods to do
that, let's take a look at Boost's.</p>
""",

"""Chapter07-1""" : """ 
	<p>Let's do something useful! It is a common case when the user's input must be checked using
some regular expression. The problem is that there are a lot of regular expression syntaxes,
expressions written using one syntax are not treated well by the other syntaxes. Another
problem is that long regexes are not so easy to write.</p>

	<p>So in this recipe, we are going to write a program that supports different regular expression
syntaxes and checks that the input strings match the specified regexes.</p>
""",

"""Chapter07-2""" : """ 
	<p>My wife enjoyed the <a href="javascript:editor.download('Chapter07', 1)">Matching strings using regular expressions</a> recipe very much. But, she
wanted more and told me that I'll get no food until I promote the recipe to be able to replace
parts of the input string according to a regex match.</p>
	<p>Ok, here it comes. Each matched sub-expression (part of the regex in parenthesis) must get a
unique number starting from 1; this number would be used to create a new string.</p>

	<p>This is how an updated program should work like:</p>
	<pre><code>
    Available regex syntaxes:
            [0] Perl
            [1] Perl case insensitive
            [2] POSIX extended
            [3] POSIX extended case insensitive
            [4] POSIX basic
            [5] POSIX basic case insensitive

    Choose regex syntax: 0
    Input regex: (\d)(\d)
    String to match: 00
    MATCH: 0, 0,
    Replace pattern: \1#\2
    RESULT: 0#0
    String to match: 42
    MATCH: 4, 2,
    Replace pattern: ###\1-\1-\2-\1-\1###
    RESULT: ###4-4-2-4-4###
</code></pre>
""",

"""Chapter07-3""" : """ 
	<p>The <code>printf</code> family of functions is a threat to security. It is a very bad design to allow
	users to put their own strings as the type and format specifiers. So what do we do when
	user-defined format is required? How shall we implement the
	<code>std::string to_string(const std::string& format_specifier) const;</code> member function
	of the following class?</p>
	<pre><code>
    class i_hold_some_internals {
        int i;
        std::string s;
        char c;
        // ...
    };
</code></pre>
""",

"""Chapter07-4""" : """ 
	<p>Situations where we need to erase something in a string, replace a part of the string, or erase
the first or last occurrence of some sub-string are very common. Standard library allows us
to do more parts of this, but it usually involves too much code writing.</p>
	<p>We saw the Boost.StringAlgorithm library in action in the <a href="javascript:editor.download('Chapter07', 0)">Changing cases and case-
	insensitive comparison</a> recipe. Let's see how it can be used to simplify our lives when we need
	to modify some strings:</p>
	<pre><code>
    #include &lt;string&gt;
    const std::string str = "Hello, hello, dear Reader.";
</code></pre>
""",

"""Chapter07-5""" : """ 
	<p>There are situations when we need to split some strings into substrings and do something
with those substrings. In this recipe, we want to split string into sentences, count characters,
and white-spaces and, of course, we want to use Boost and be as efficient as possible.</p>
""",

"""Chapter07-6""" : """ 
	<p>This recipe is the most important recipe in this chapter! Let's take a look at a very common
case, where we write some function that accepts a string and returns a part of the string
between character values passed in the <code>starts</code> and <code>ends</code> arguments:</p>
	<pre><code>
    #include &lt;string&gt;
    #include &lt;algorithm&gt;
    std::string between_str(const std::string&amp; input, char starts, char ends) {
        std::string::const_iterator pos_beg
            = std::find(input.begin(), input.end(), starts);

        if (pos_beg == input.end()) {
            return std::string(); // Empty
        }
        ++ pos_beg;
        std::string::const_iterator pos_end
            = std::find(input.begin(), input.end(), ends);

        return std::string(pos_beg, pos_end);
    }
</code></pre>
	<p>Do you like this implementation? In my opinion, it looks awful. Consider the following call to it:</p>
	<pre><code>
    between_str("Getting expression (between brackets)", '(', ')');
</code></pre>

	<p>In this example, a temporary<code>std::string</code> variable is constructed from <code>"Getting
expression (between brackets)"</code>. The character array is long enough, so there is a big
chance that dynamic memory allocation is called inside the <code>std::string</code> constructor and
the character array is copied into it. Then, somewhere inside the<code>between_str</code>
function, new <code>std::string</code> is being constructed, which may also lead to another dynamic memory
allocation and copying.</p>
	<p>So, this simple function may, and in most cases will:</p>
	<p> * Call dynamic memory allocation (two times)</p>
	<p> * Copy string (two times)</p>
	<p> * Deallocate memory (two times)</p>

	<br><p>Can we do better?</p>
""",


"""Chapter08-0""" : """ 
	<p>There are situations when it would be great to work with all the template parameters like
they were in a container. Imagine that we are writing something, such as Boost.Variant:</p>
	<pre><code>
    #include &lt;boost/mpl/aux_/na.hpp&gt;  // boost::mpl::na == n.a. == not available

    template &lt;
        class T0 = boost::mpl::na,
        class T1 = boost::mpl::na,
        class T2 = boost::mpl::na,
        class T3 = boost::mpl::na,
        class T4 = boost::mpl::na,
        class T5 = boost::mpl::na,
        class T6 = boost::mpl::na,
        class T7 = boost::mpl::na,
        class T8 = boost::mpl::na,
        class T9 = boost::mpl::na
    &gt;
    struct variant;
</code></pre>
	<p>The preceding code is the place where all the following interesting tasks start to happen:</p>
	<p> * How can we remove constant and volatile qualifiers from all the types?</p>
	<p> * How can we remove duplicate types?</p>
	<p> * How can we get the sizes of all the types?</p>
	<p> * How can we get the maximum size of the input parameters?</p>
	<p>All these tasks can be easily solved using Boost.MPL.</p>
""",


"""Chapter08-1""" : """ 
	<p>The task of this recipe is to modify the content of one <code>boost::mpl::vector</code> type
depending on the content of a second <code>boost::mpl::vector</code> type. We'll be calling
the second vector as the vector of modifiers and each of those modifiers can have the
following type:</p>
	<pre><code>
    // Make unsigned
    struct unsigne; // No typo: 'unsigned' is a keyword, we cannot use it.
    // Make constant
    struct constant;
    // Otherwise we do not change type
    struct no_change;
</code></pre>
	<p>So where shall we start from?</p>
""",

"""Chapter08-2""" : """ 
	<p>Many good features were added to C++11 to simplify the metaprogramming. One such
feature is the alternative function syntax. It allows deducing the result type of a template
function. Here is an example:</p>
	<pre><code>
    template &lt;class T1, class T2&gt;
    auto my_function_cpp11(const T1&amp; v1, const T2&amp; v2)
        -&gt; decltype(v1 + v2)
    {
        return v1 + v2;
    }
</code></pre>
	<p>It allows us to write generic functions more easily:</p>
	<pre><code>
    #include &lt;cassert&gt;
    struct s1 {};
    struct s2 {};
    struct s3 {};

    inline s3 operator + (const s1&amp; /*v1*/, const s2&amp; /*v2*/) {
        return s3();
    }

    inline s3 operator + (const s2&amp; /*v1*/, const s1&amp; /*v2*/) {
        return s3();
    }

    int main() {
        s1 v1;
        s2 v2;
        my_function_cpp11(v1, v2);
        my_function_cpp11(v1, v2);
        assert(my_function_cpp11('\0', 1) == 1);
    }
</code></pre>
	<p>But, Boost has a lot of functions like these and it does not require C++11 to work. How is
that possible and how can we make a C++03 version of the
<code>my_function_cpp11</code> function?</p>
""",


"""Chapter08-3""" : """ 
	<p>Functions that accept other functions as an input parameter or functions that return
	other functions are called higher-order functions. For example, the following functions
	are higher-order:</p>
	<pre><code>
    function_t higher_order_function1();
    void higher_order_function2(function_t f);
    function_t higher_order_function3(function_t f);
</code></pre>
	<p>We have already seen higher-order metafunctions in the recipes <a href="javascript:editor.download('Chapter08', 0)">Using type "vector of types"</a>
	and <a href="javascript:editor.download('Chapter08', 1)">Manipulating a vector of types</a> from this chapter, where we used <code>boost::transform</code>.</p>

	<p>In this recipe, we'll try to make our own higher-order metafunction named <code>coalesce</code>,
	which accepts two types and two metafunctions. The coalesce metafunction applies
	the first type-parameter to the first metafunction and compares the resulting type
	with the <code>boost::mpl::false_</code> type metafunction. If the resulting type is the
	<code>boost::mpl::false_</code> type metafunction, it returns the result of applying the second
	type-parameter to the second metafunction, otherwise, it returns the first result type:</p>
	<pre><code>
    template &lt;class Param1, class Param2, class Func1, class Func2&gt;
    struct coalesce;
</code></pre>
""",

"""Chapter08-4""" : """ 
	<p>Lazy evaluation means that the function is not called until we really need its result.
Knowledge of this recipe is highly recommended for writing good metafunctions. The
importance of lazy evaluation will be shown in the following example.</p>
	<p>Imagine that we are writing some metafunction that accepts a function Func , a parameter
Param , and a condition Cond . The resulting type of that function must be a fallback type
if applying the Cond to Param returns false , otherwise the result must be a Func applied
to Param :</p>
	<pre><code>
    struct fallback;
    template &lt;
        class Func,
        class Param,
        class Cond,
        class Fallback = fallback&gt;
    struct apply_if;
</code></pre>
	<p>This metafunction is the place where we cannot live without lazy evaluation, because it may
be impossible to apply Func to Param if the Cond is not met. Such attempts will always
result in compilation failure and Fallback is never returned.</p>
""",

"""Chapter08-5""" : """ 
	<p>This recipe and the next one are devoted to a mix of compile time and runtime features.
We'll be using the Boost.Fusion library and see what it can do.</p>
	<p>Remember that we were talking about tuples and arrays in the first chapter? Now, we want
to write a single function that can stream elements of tuples and arrays to strings.</p>
""",


"""Chapter08-6""" : """ 
	<p>This recipe will show a tiny piece of the Boost.Fusion library's abilities. We'll be splitting
a single tuple into two tuples, one with arithmetic types and the other with all other types.</p>
""",

"""Chapter08-7""" : """ 
	<p>Most of the metaprogramming tricks that we saw in this chapter were invented long before
C++11. Probably, you've already heard about some of that stuff.</p>
	<p>How about something brand new? How about implementing the previous recipe in C++14
with a library that puts the metaprogramming upside down and makes your eyebrows go
up? Fasten your seatbelts, we're diving into the world of Boost.Hana .</p>
""",




"""Chapter09-0""" : """ 
	<p>For the past two decades, C++ programmers were using std::vector as a default
sequence container. It is a fast container that does not do a lot of allocations, stores elements
in a CPU cache friendly way and because container stores the elements contiguously
<code>std::vector::data()</code> like functions allows to inter-operate with pure C functions.</p>
	<p>But, we want more! There are cases when we do know the typical elements count to store in
the vector, and we need to improve the performance of the vector by totally eliminating the
memory allocations for that case.</p>
	<p>Imagine that we are writing a high performance system for processing bank transactions.
Transaction is a sequence of operations that must all succeed or fail if at least one of the
operations failed. We know that the 99% of transactions consist of 8 or less operations and
wish to speed up things:</p>
	<pre><code>
    #include &lt;vector&gt;

    class operation;
    template &lt;class T&gt;
    void execute_operations(const T&amp;);

    bool has_operation();
    operation get_operation();

    void process_transaction_1() {
        std::vector&lt;operation&gt; ops;
        ops.reserve(8); // TODO: Memory allocation. Not good!

        while (has_operation()) {
            ops.push_back(get_operation());
        }

        execute_operations(ops);
        // ...
    }
</code></pre>
""",

"""Chapter09-1""" : """ 
	<p>Here's a question: what container should we use to return the sequence from function if we
know that the sequence never has more than N elements and N is not big. For example, how
we must write the <code>get_events()</code> function that returns at most five events:</p>
	<pre><code>
    #include &lt;vector&gt;

    std::vector&lt;event&gt; get_events();
</code></pre>
	<p>The <code>std::vector&lt;event&gt;</code> allocates memory, so the code from earlier is not a good
solution.</p>
	<pre><code>
    #include &lt;boost/array.hpp&gt;

    boost::array&lt;event, 5&gt; get_events();
</code></pre>
	<p><code>boost::array&lt;event, 5&gt;</code>does not allocate memory, but it constructs all the five
elements. There's no way to return less than five elements.</p>
	<pre><code>
    #include &lt;boost/container/small_vector.hpp&gt;

    boost::container::small_vector&lt;event, 5&gt; get_events();
</code></pre>
	<p>The <code>boost::container::small_vector&lt;event, 5&gt;</code> does not allocate memory for five
or less elements and allows us to return less than five elements. However, the solution is
not perfect, because it is not obvious from the function interface that it never returns more
than five elements.</p>
""",

"""Chapter09-2""" : """ 
	<p>It is a common task to manipulate strings. Here, we'll see how an operation of string
comparison can be done quickly using some simple tricks. This recipe is a trampoline for
the next one, where the techniques described here will be used to achieve constant time-
complexity searches.</p>
	<p>So, we need to make some class that is capable of quickly comparing strings for equality.</p>
""",

"""Chapter09-3""" : """ 
	<p>In the previous recipe, we saw how string comparison can be optimized using hashing.
After reading it, the following question may arise: can we make a container that will cache
hashed values to use faster comparison?</p>
	<p>The answer is yes, and we can do much more. We may achieve almost constant search,
insertion, and removal times for elements.</p>
""",

"""Chapter09-4""" : """ 
	<p>Several times in a year, we need something that may store and index a pair of values.
Moreover, we need to get the first part of the pair using the second, and get the second part
using the first. Confused? Let me show you an example. We create a vocabulary class.
When the users put values into it, the class must return identifiers, and when the users put
identifiers into it, the class must return values.</p>
	<p>To be more practical, users are putting login names in our vocabulary and wish to get the
unique identifier out of it. They also wish to get all the logins for an identifier.</p>
	<p>Let's see how it can be implemented using Boost.</p>
""",

"""Chapter09-5""" : """ 
	<p>In the previous recipe, we made some kind of vocabulary, which is good when we need to
work with pairs. But, what if we need much more advanced indexing? Let's make a
program that indexes persons:</p>
	<pre><code>
    struct person {
        std::size_t     id_;
        std::string     name_;
        unsigned int    height_;
        unsigned int    weight_;

        person(std::size_t id, const std::string& name, unsigned int height, unsigned int weight)
            : id_(id)
            , name_(name)
            , height_(height)
            , weight_(weight)
        {}
    };

    inline bool operator &lt; (const person& p1, const person& p2) {
        return p1.name_ &lt; p2.name_;
    }
</code></pre>
	<p>We will need a lot of indexes, for example, by name, ID, height, and weight.</p>
""",

"""Chapter09-6""" : """ 
	<p>Nowadays, we usually use <code>std::vector</code> when we need nonassociative and nonordered
containers. This is recommended by Andrei Alexandrescu and Herb Sutter in the book
C++ Coding Standards. Even those users who did not read the book usually use
<code>std::vector</code>. Why? Well, <code>std::list</code> is slower, and uses much more resources than
<code>std::vector</code>. The <code>std::deque</code> container is very close to <code>std::vector</code>, but does not store values
continuously.</p>
	<p>If we need a container where erasing and inserting elements does not invalidate iterators,
then we are forced to choose a slow <code>std::list</code>.</p>
	<p>But wait, we may assemble a better solution using Boost!</p>
""",

"""Chapter09-7""" : """ 
	<p>After reading the previous recipe, some of the readers may start using fast pool allocators
everywhere; especially, for <code>std::set</code> and <code>std::map</code>. Well, I'm not going to stop you from
doing that, but at least let's take a look at an alternative: flat associative containers. These
containers are implemented on top of the traditional vector container and store the values
ordered.</p>
""",




"""Chapter10-0""" : """ 
	<p>I'm guessing you've seen a bunch of ugly macros to detect the compiler on which the code is
compiled. Something like this is a typical practice in C word:</p>
<pre><code>
    #include &lt;something_that_defines_macros&gt;

    #if !defined(__clang__) \
        &amp;&amp; !defined(__ICC) \
        &amp;&amp; !defined(__INTEL_COMPILER) \
        &amp;&amp; (defined(__GNUC__) || defined(__GNUG__))

    // GCC specific

    #endif
</code></pre>
	<p>Now, try to come up with a good macro to detect the GCC compiler. Try to make that
macro usage as short as possible.</p>
	<p>Take a look at the following recipe to verify your guess.</p>
""",

"""Chapter10-1""" : """ 
	<p>Some compilers have support for extended arithmetic types such as 128 bit floats or
integers. Let's take a quick glance at how to use them using Boost.</p>
	<p>We'll be creating a method that accepts three parameters and returns the multiplied value of
those methods. If compiler supports 128-bit integers, then we use them. If compiler
supports <code>long long</code>,then we use it; otherwise, we need to issue a compile-time error.</p>
""",

"""Chapter10-2""" : """ 
	<p>Some companies and libraries have specific requirements for their C++ code, such as
successful compilation without RTTI.</p>
	<p>In this small recipe, we'll not just detect disabled RTTI, but also write a Boost like library
from scratch that stores information about types, and compares types at runtime, even
without <code>typeid</code>.</p>
""",

"""Chapter10-3""" : """ 
	<p><a href='javascript:$("#chapters-link").click();'>Chapter 4, Compile-time Tricks</a>, and <a href='javascript:$("#chapters-link").click();'>Chapter 8, Metaprogramming</a>, were devoted to
	metaprogramming. If you were trying to use techniques from those chapters, you may
	have noticed that writing a metafunction can take a lot of time. So it may be a good idea
	to experiment with metafunctions using more user-friendly methods, such as C++11
	constexpr , before writing a portable implementation.</p>
	<p>In this recipe, we'll take a look at how to detect <code>constexpr</code> support.</p>
""",

"""Chapter10-4""" : """ 
	<p>C++11 has very specific logic when user-defined types (UDTs) are used in standard library
containers. Some containers use move assignment and move construction only if the move
constructor does not throw exceptions or there is no copy constructor.</p>
	<p>Let's see how we can ensure the compiler that the out class move_nothrow has a non-
throwing move assignment operator and a non-throwing move constructor.</p>
""",


"""Chapter10-5""" : """ 
	<p>Almost all modern languages have the ability to make libraries, a collection of classes, and
methods that have a well-defined interface. C++ is no exception to this rule. We have two
types of libraries: runtime (also called shared or dynamic) and static. But, writing libraries is
not a simple task in C++. Different platforms have different methods for describing which
symbols must be exported from the shared library.</p>
	<p>Let's take a look at how to manage symbol visibility in a portable way using Boost.</p>
""",

"""Chapter10-6""" : """ 
	<p>Boost is being actively developed, so each release contains new features and libraries. Some
people wish to have libraries that compile for different versions of Boost and also want to
use some of the features of the new versions.</p>
	<p>Let's take a look at the <code>boost::lexical_cast</code> change log. According to it, Boost 1.53 has
a <code>lexical_cast(const CharType* chars, std::size_t count)</code> function overload.
Our task for this recipe will be to use that function overload for new versions of Boost, and
work around that missing function overload for older versions.</p>
""",






"""Chapter11-0""" : """ 
	<p>There are standard library functions and classes to read and write data to files. But before
C++17, there were no functions to list files in a directory, get the type of a file, or get access
rights for a file.</p>
	<p>Let's see how such iniquities can be fixed using Boost. We'll be doing a program that lists
names, write accesses, and types of files in the current directory.</p>
""",

"""Chapter11-1""" : """ 
	<p>Let's consider the following lines of code:</p>
	<pre><code>
    std::ofstream ofs("dir/subdir/file.txt");
    ofs &lt;&lt; "Boost.Filesystem is fun!";
</code></pre>
	<p>In these lines, we attempt to write something to file.txt in the dir/subdir directory.
This attempt will fail if there is no such directory. The ability to work with filesystems is
necessary for writing a good working code.</p>

	<p>In this recipe, we'll construct a directory and a subdirectory, write some data to a file, and
try to create symlink . If the symbolic link's creation fails, erase the created entities. We
should also avoid using exceptions as a mechanism of error reporting, preferring some kind
of return codes.</p>
	<p>Let's see how that can be done in an elegant way using Boost.</p>
""",

"""Chapter11-2""" : """ 
	<p>Here's a tricky question: we want to allow users to write extensions to the functionality of
our program, but we do not want to give them the source codes. In other words we'd like to
say, "Write a function X and pack it into a shared library. We may use your function along with
functions of some other users!"</p>
	<p>You meet this technique in everyday life: your browser uses it to allow
third-party plugins, your text editor may use it for syntax highlighting,
games use dynamic library loading for downloadable content (DLCs)
and for adding gamer's content, web pages are returned by servers that
use modules/plugins for encryption/authentication and so forth.</p>
	<p>What are the requirements for a user's function and how can we use that function at some
point without linking it to the shared library?</p>
""",


"""Chapter11-3""" : """ 
	<p>When reporting errors or failures, it is more important to report the steps that lead to the
error rather than the error itself. Consider the naive trading simulator:</p>
	<pre><code>
    int main() {
        int money = 1000;
        start_trading(money);
    }
</code></pre>
	<p>All it reports is a line:</p>
	<pre><code>
    Sorry, you're bankrupt!
</code></pre>
	<p>That's a no go. We want to know how did it happened, what were the steps that led to
bankruptcy!</p>
	<p>Okay. Let's fix the following function and make it report the steps that led to bankruptcy:</p>
	<pre><code>
    void report_bankruptcy() {
        std::cout &lt;&lt; "Sorry, you're bankrupt!\n";
        std::exit(0);
    }
</code></pre>
""",

"""Chapter11-4""" : """ 
	<p>Sometimes, we write programs that communicate with each other a lot. When programs are
run on different machines, using sockets is the most common technique for communication.
But if multiple processes run on a single machine, we can do much better!</p>
	<p>Let's take a look at how to make a single memory fragment available from different
processes using the Boost.Interprocess library.</p>
""",

"""Chapter11-5""" : """ 
	<p>In the previous recipe, we saw how to create shared memory and how to place some objects in
it. Now it's time to do something useful. Let's take an example from the <a href="javascript:editor.download('Chapter05', 3)">Creating a work_queue class</a>
recipe, and make it work for multiple processes. At the end of
this example, we'll get a class that can store different tasks and pass them between processes.</p>
""",

"""Chapter11-6""" : """ 
	<p>It is hard to imagine writing some C++ core classes without pointers. Pointers and references
are everywhere in C++, and they do not work in shared memory! So if we have a structure like
this in shared memory and assign the address of some integer variable in shared memory
to <code>pointer_</code>, we won't get the correct address in the other process that will attempt to use
<code>pointer_</code> from that instance of <code>with_pointer</code>:</p>
	<pre><code>
    struct with_pointer {
        int* pointer_;
        // ...
        int value_holder_;
    };
</code></pre>
	<p>How can we fix that?</p>
""",

"""Chapter11-7""" : """ 
	<p>All around the Internet, people are asking "What is the fastest way to read files?". Let's
make our task for this recipe even harder: "What is the fastest and most portable way to
read binary files?"</p>
""",


"""Chapter11-8""" : """ 
	<p>Nowadays, plenty of embedded devices still have only a single core. Developers write for
those devices, trying to squeeze maximum performance out of them.</p>
	<p>Using Boost.Threads or some other thread library for such devices is not effective. The
OS will be forced to schedule threads for execution, manage resources, and so on, as the
hardware cannot run them in parallel.</p>
	<p>So, how can we force a program to switch to the execution of a subprogram while waiting
for some resource in the main part? Moreover, how can we control the time of the
subprogram's execution?</p>
""",



"""Chapter12-0""" : """ 
	<p>Some tasks require representing data as a graph. The Boost.Graph is a library that was
designed to provide a flexible way of constructing and representing graphs in memory. It
also contains a lot of algorithms to work with graphs, such as topological sort, breadth first
search, depth first search, and Dijkstra shortest paths.</p>
	<p>Well, let's perform some basic tasks with Boost.Graph !</p>
""",

"""Chapter12-1""" : """ 
	<p>Making programs that manipulate graphs was never easy because of issues with
visualization. When we work with standard library containers such as <code>std::map</code> and
<code>std::vector</code>, we can always print the container's contents and see what is going on inside.
But when we work with complex graphs, it is hard to visualize the content in a clear way;
textual representation is not human friendly because it typically contains too many vertexes
and edges.</p>
	<p>In this recipe, we'll take a look at the visualization of Boost.Graph using the Graphviz
tool.</p>
""",

"""Chapter12-2""" : """ 
	<p>I know of many examples of commercial products that use incorrect methods for getting
random numbers. It's a shame that some companies still use rand() in cryptography and
banking software.</p>
	<p>Let's see how to get a fully random uniform distribution using Boost.Random that is
suitable for banking software.</p>
""",

"""Chapter12-3""" : """ 
	<p>Some projects require specific trigonometric functions, a library for numerically solving
ordinary differential equations and working with distributions and constants. All those
parts of Boost.Math will be hard to fit even in a separate book. A single recipe definitely
won't be enough. So, let's focus on very basic everyday-use functions to work with float
types.</p>
	<p>We'll write a portable function that checks an input value for infinity and not-a-number (<code>NaN</code>)
values and changes the sign if the value is negative.</p>
""",

"""Chapter12-4""" : """ 
	<p>This recipe and the next one are devoted to auto-testing using the Boost.Test library,
which is used by many Boost libraries. Let's get hands-on with it and write some tests for
our own class.</p>
""",

"""Chapter12-5""" : """ 
	<p>Writing auto tests is good for your project. However, managing test cases is hard when the
project is big and many developers work on it. In this recipe, we'll take a look at how to run
individual tests and how to combine multiple test cases in a single module.</p>
	<p>Let's pretend that two developers are testing the foo structure declared in the foo.hpp
header and we wish to give them separate source files to write tests to. In that case, both
developers won't bother each other and may work in parallel. However, the default test run
must execute tests of both developers.</p>
""",

"""Chapter12-6""" : """ 
	<p>I've left you something really tasty for dessert - Boost's Generic Image Library or just
Boost.GIL , which allows you to manipulate images without worrying too much about
image formats.</p>
	<p>Let's do something simple and interesting with it. For example, let's make a program that
negates any picture.</p>
""",
};
