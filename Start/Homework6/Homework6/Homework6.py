import string
from math import pi
from regex import regex

if __name__ == '__main__':
    print("Exercise 1:")
    x = input("String: ")
    count = 0
    for item in x:
        if item == "b":
            count += 1
    print("Count is ", count)

    print("\nExercise 2:")
    name = input("Name: ")
    for item in string.digits:
        if not name.istitle() or item in name:
            print("Incorrect name!")
            break

    print("\nExercise 3:")
    x = "Hello, world!"
    summary = 0
    for item in x:
        summary += ord(item)
    print("Sum is ", summary)
    
    print("\nExercise 4:")
    count = 10
    x = f"{pi}"
    for i in range(count):
        print(x[:(i + 4)])

    print("\nExercise 5:")
    x = input("String: ")
    x = x.split(" ")
    print(max(x, key = len))
    
    print("\nExtra Exercise 1:")
    text = "artartartartartartart ititititit catcatcatcat"
    print(text)
    text = text.split(" ")
    for i in range(len(text)):
        text[i] = text[i][:len(set(text[i]))]
    print("Min word is ", min(text, key = len))

    print("\nExtra Exercise 2:")
    text = """
<div itemprop="articleBody"> <!--noindex--><div id="toc_container" class="no_bullets" style="width: auto; display: table;"><p class="toc_title">Содержание <span class="toc_toggle">[<a href="#">Скрыть</a>]</span></p><ul class="toc_list" style="display: block;"><li><a href="#1"><span class="toc_number toc_depth_1">1</span> 1. </a></li><li><a href="#2"><span class="toc_number toc_depth_1">2</span> 2. </a></li><li><a href="#3"><span class="toc_number toc_depth_1">3</span> 3. </a></li><li><a href="#4"><span class="toc_number toc_depth_1">4</span> 4. </a></li><li><a href="#5"><span class="toc_number toc_depth_1">5</span> 5. </a></li><li><a href="#6"><span class="toc_number toc_depth_1">6</span> 6. </a></li><li><a href="#7"><span class="toc_number toc_depth_1">7</span> 7. </a></li><li><a href="#____________Big_and_Important_Header_Slightly_Less_Big_Header"><span class="toc_number toc_depth_1">8</span> определяет заголовки второго уровня, <!--/noindex-->
третий уровень и так далее, вплоть до. Например, имена тегов в этой статье являются заголовками второго уровня.
Big and Important Header
Slightly Less Big Header</a><ul><li><a href="#Sub-Header"><span class="toc_number toc_depth_2">8.1</span> Sub-Header</a></li></ul></li><li><a href="#i"><span class="toc_number toc_depth_1">9</span> Чуть менее большой заголовок</a><ul><li><a href="#Sub-Header-2"><span class="toc_number toc_depth_2">9.1</span> Sub-Header</a></li></ul></li><li><a href="#8"><span class="toc_number toc_depth_1">10</span> 8. </a></li><li><a href="#9"><span class="toc_number toc_depth_1">11</span> 9. </a></li><li><a href="#10"><span class="toc_number toc_depth_1">12</span> 10. </a></li><li><a href="#11"><span class="toc_number toc_depth_1">13</span> 11. </a></li><li><a href="#12"><span class="toc_number toc_depth_1">14</span> 12. </a></li><li><a href="#13"><span class="toc_number toc_depth_1">15</span> 13. </a></li><li><a href="#14"><span class="toc_number toc_depth_1">16</span> 14. </a></li><li><a href="#15"><span class="toc_number toc_depth_1">17</span> 15. </a></li><li><a href="#16"><span class="toc_number toc_depth_1">18</span> 16. </a></li><li><a href="#17"><span class="toc_number toc_depth_1">19</span> 17. </a></li><li><a href="#_HTML"><span class="toc_number toc_depth_1">20</span> Вперед и HTML</a></li></ul></div><p>Несмотря на то, что современные веб-сайты обычно создаются с дружественными интерфейсами</p><script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-8069845134488215" data-ad-slot="5512937869" data-ad-format="auto" data-full-width-responsive="true"><iframe id="aswift_0" style="height: 1px !important; max-height: 1px !important; max-width: 1px !important; width: 1px !important;"><iframe id="google_ads_frame0"></iframe></iframe></ins>
<script>
</script><p>все еще хорошо знать некоторый основной HTML. Если вы знаете следующие 17 тегов (и несколько дополнительных, которые идут с ними), вы сможете создать базовую веб-страницу с нуля или настроить код, созданный приложением, таким как WordPress.</p><p>,</p><p>Я предоставил примеры для большинства тегов, но если вы хотите увидеть их в действии, загрузите связанный HTML-файл в конце статьи. Вы можете поиграть с ним в текстовом редакторе и загрузить его в браузере, чтобы увидеть, что делают ваши изменения.</p><h2><span id="1">1. </span></h2><p>Этот тег вам понадобится в начале каждого HTML-документа, который вы создаете. Это гарантирует, что браузер знает, что он читает HTML, и что он ожидает HTML5, последнюю версию</p><script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-8069845134488215" data-ad-slot="5512937869" data-ad-format="auto" data-full-width-responsive="true"><iframe id="aswift_1" style="height: 1px !important; max-height: 1px !important; max-width: 1px !important; width: 1px !important;"><iframe id="google_ads_frame1"></iframe></iframe></ins>
<script>
</script><p>,</p><p>Несмотря на то, что это на самом деле не HTML-тег, его все же стоит знать.</p><p> <noscript><img src="/wp-content/uploads/2009/7/17-prostyh-primerov-koda-html-kotorye-vy-mozhete_1.png" alt="Пример HTML-кода" /></noscript><img class=" lazyloaded" src="/wp-content/uploads/2009/7/17-prostyh-primerov-koda-html-kotorye-vy-mozhete_1.png" data-src="/wp-content/uploads/2009/7/17-prostyh-primerov-koda-html-kotorye-vy-mozhete_1.png" alt="Пример HTML-кода">Изображение предоставлено: Юрич через Shutterstock</p><h2><span id="2">2. </span></h2><p>Это еще один тег, который сообщает браузеру, что он читает HTML. Зачем нам оба? Кто знает? Но в любом случае это хорошая идея.</p><p>И в конце вашего документа добавьте тег.</p><script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-8069845134488215" data-ad-slot="5512937869" data-ad-format="auto" data-full-width-responsive="true"><iframe id="aswift_2" style="height: 1px !important; max-height: 1px !important; max-width: 1px !important; width: 1px !important;"><iframe id="google_ads_frame2"></iframe></iframe></ins>
<script>
</script><h2><span id="3">3. </span></h2><p>Для основных страниц тег будет содержать ваш заголовок, и это все. Но есть несколько других вещей, которые вы можете включить, о которых мы поговорим чуть позже.</p><h2><span id="4">4. </span></h2><p>Как и следовало ожидать, это определяет заголовок вашей страницы. Все, что вам нужно сделать, это поместить свой заголовок в тег и закрыть его следующим образом (я также включил теги заголовка):</p><pre><code>
My Website
</code></pre><p>Это имя, которое будет отображаться в виде заголовка вкладки при его открытии в браузере.</p><p><noscript><img src="/wp-content/uploads/2009/7/17-prostyh-primerov-koda-html-kotorye-vy-mozhete_1_1.png" alt="тег заголовка HTML" /></noscript><img class=" lazyloaded" src="/wp-content/uploads/2009/7/17-prostyh-primerov-koda-html-kotorye-vy-mozhete_1_1.png" data-src="/wp-content/uploads/2009/7/17-prostyh-primerov-koda-html-kotorye-vy-mozhete_1_1.png" alt="тег заголовка HTML"></p><h2><span id="5">5. </span></h2><p>Как и тег заголовка, метаданные помещаются в область заголовка вашей страницы (эти метаданные, в отличие от метаданных с мобильных устройств).</p><script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

"""
    res = regex.sub('<[^<]+?>', '', text)
    print(res)

        
    

    
